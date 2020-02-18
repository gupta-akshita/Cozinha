from django import template
from cart.models import Cart, CartItem

register = template.Library()
@register.simple_tag
def cart_total_items(request):

    if request.user.is_authenticated:
        data = Cart.objects.get(user=request.user)
        total_item = data.cartitem_set.count()
        return total_item
                
    else:
        if 'cart' in request.session.keys():
            total_item = len(request.session['cart'])
            return total_item
        else:
            return 0