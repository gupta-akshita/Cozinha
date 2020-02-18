from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from products.models import Product
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django import template
from products.models import Product
from .models import Cart, CartItem

user = get_user_model()   

class AddToCart(View):  

    def post(self, request):                

        if request.user.is_authenticated:
            pk = int(request.POST['id'])  
            quantity = int(request.POST['count'])
            data = Cart.objects.get(user=request.user)
            product = Product.objects.get(pk=pk) 
            try:
                item = data.cartitem_set.get(product__id=pk)
                if quantity == 0:
                    item.delete()
                else:
                    item.quantity = quantity
                    item.save()
                return JsonResponse({"message":"success"})
            except CartItem.DoesNotExist:                
                data = CartItem.objects.create(cart=data, quantity=quantity, product=product)
                return JsonResponse({"message":"success"})
    
        else:
            check = 0
            pk = int(request.POST['id'])  
            count = int(request.POST['count']) 
            shop = Product.objects.get(pk=pk)

            if 'cart' not in self.request.session.keys(): 
                self.request.session['cart'] = []
                self.request.session['cart'].append({'id': pk, 'quantity': count})
                self.request.session.save()                
                return JsonResponse({"message":"success"})
                
            else:
                for x in self.request.session['cart']:
                    if pk == x['id']:
                        check = 1
                        x['quantity'] = count
                        break
                if check == 0:
                    self.request.session['cart'].append({'id': pk,'quantity': count})
                self.request.session.save()
                print("-----------SESSION----------",self.request.session['cart'])  
                return JsonResponse({"message":"success"})

class CartView(TemplateView):
    template_name = 'cart.html'

class GetData(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            data = Cart.objects.get(user=request.user)
            total_items = data.cartitem_set.count()
            return JsonResponse({"total_items": total_items})

        else:
            if 'cart' in self.request.session.keys():
                total_items = len(self.request.session['cart'])
                return JsonResponse({"total_items": total_items})





