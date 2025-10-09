from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.utils.http import urlencode
from django.core.cache import cache
from .models import Product
# Create your views here.




class HomeView(ListView):
    template_name = "home/home.html"
    context_object_name = "products"
    def get_queryset(self):
        return Product.objects.all().order_by("-created_at")[:8]


class AboutView(TemplateView):
    template_name = "home/about.html"



class ProductsView(ListView):
    model = Product
    template_name = "home/products.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        cache.set("name","matin",timeout=500)
        return super().get_queryset()

class ProductDetailView(DetailView):
    model = Product
    template_name = "home/product_detail.html"
    context_object_name = "product"


class FaqView(TemplateView):
    template_name = "home/faq.html"