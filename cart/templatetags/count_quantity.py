from django import template
from cart.models import Cart, CartItem

register = template.Library()
@register.simple_tag
def count_quantity(request, id):
    
    if request.user.is_authenticated:
        data = Cart.objects.get(user=request.user)
        try:
            item = data.cartitem_set.get(product__id=id)
            quantity = item.quantity
            return quantity
        except CartItem.DoesNotExist:
            return 0
                
    else:
        check = 0
        if 'cart' in request.session.keys():
            for x in request.session['cart']:
                if id == x['id']:
                    check = 1
                    return x['quantity']
            if check == 0 :
                return 0
        else:
            return 0


