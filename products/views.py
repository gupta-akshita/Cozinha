from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product

class Shops(TemplateView):
    template_name = 'shops.html'
    
    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['data'] = Product.objects.filter(pshop__id=pk)
        return context

