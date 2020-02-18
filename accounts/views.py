from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import auth
from cart.models import Cart, CartItem
from products.models import Product

User = get_user_model()

# Create your views here.

class SignUp(CreateView):
    template_name = 'signup.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        form = SignUpForm(data=request.POST)
        if form.is_valid(): 
            user = User.objects.create_user(email = request.POST['email'], password=request.POST['password'], phone=request.POST['phone'], first_name=request.POST['first_name'], last_name=request.POST['last_name'] )
            if 'cart' in self.request.session.keys():
                cart_data = self.request.session['cart']   
            else:
                cart_data = None        
            auth.login(request, user)
            cart = Cart.objects.create(user=user)
            
            if cart_data:
                for x in cart_data:
                    product_id = x['id']
                    quantity = x['quantity']
                    product = Product.objects.get(pk=product_id)
                    data = CartItem.objects.create(cart=cart, quantity=quantity, product=product)
                del self.request.session['cart']
            return redirect('index')
        else:
            return render(request, self.template_name, {'form':SignUpForm})
        

class SignIn(TemplateView):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name, {'error':'Not'})

    def post(self, request):
        user = auth.authenticate(email= request.POST['email'], password=request.POST['password'])
        if user is not None:
            if 'cart' in self.request.session.keys():
                cart_data = self.request.session['cart']
                auth.login(request, user)            
                cart = Cart.objects.get(user=user)
                for x in cart_data:
                    product_id = x['id']
                    quantity = x['quantity']
                    product = Product.objects.get(pk=product_id)
                    try:
                        item = cart.cartitem_set.get(product__id=product_id)
                        item.quantity += quantity
                        item.save()
                    except CartItem.DoesNotExist:
                        data = CartItem.objects.create(cart=cart, quantity=quantity, product=product)
                del self.request.session['cart']
            else:
                auth.login(request, user)
            return redirect('index')

            
        else:
            return render(request, self.template_name, {'error':'username or password is incorrect.'})


class LogOut(TemplateView):
    
    def get(self, request):
        auth.logout(request)
        return redirect('index')