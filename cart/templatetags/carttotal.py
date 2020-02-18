from django import template
from cart.models import Cart, CartItem
from products.models import Product

register = template.Library()
@register.simple_tag
def carttotal(request):
    if request.user.is_authenticated:
        data = Cart.objects.get(user=request.user)
        carttotal = 0
        for x in data.cartitem_set.all():
            carttotal += (x.quantity*x.product.pprice)
        return carttotal

    else:
        if 'cart' in request.session.keys():
            carttotal = 0
            for x in request.session['cart']:
                import pdb; pdb.set_trace()
                product = Product.objects.get(id=x['id'])
                carttotal += (x['quantity']*product.pprice)
            return carttotal