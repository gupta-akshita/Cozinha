from django import template
from cart.models import Cart, CartItem  
from products.models import Product

register = template.Library()
@register.simple_tag
def cart(request):
    
    if request.user.is_authenticated:
        data = Cart.objects.get(user=request.user)
        try:
            item = data.cartitem_set.all()
            return item
        except CartItem.DoesNotExist:
            return None

    else:
        if 'cart' in request.session.keys():
            item = request.session['cart']
            for x in item:
                x['id'] = Product.objects.get(id=x['id'])
            import pdb; pdb.set_trace()
            return item
        else:
            return None
