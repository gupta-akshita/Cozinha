from django.views.generic import TemplateView
from shops.models import Shop
from products.models import Product
from django.forms.models import model_to_dict


class HomeView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		# del self.request.session['cart']	
		print("------SESSION----------", self.request.session.keys())
		if('cart' in self.request.session.keys()):
			print("-----------CART--------------", self.request.session['cart'])
		context = super().get_context_data(**kwargs)
		context['shop'] = Shop.objects.all()
		return context
