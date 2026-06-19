from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from .models import Product,Category
# Create your views here.




class HomeView(ListView):
    template_name = "home/home.html"
    context_object_name = "products"
    
    def get_queryset(self):
        return Product.objects.order_by("-created_at")[:8]

class AboutView(TemplateView):
    template_name = "home/about.html"



class ProductsView(ListView):
    model = Product
    template_name = "home/products.html"
    context_object_name = "products"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    def get_queryset(self):
        if self.kwargs.get("slug"):
            return Product.objects.filter(
                category__slug=self.kwargs["slug"]
            ).order_by("id")
        return Product.objects.all().order_by("id")
    

class ProductDetailView(DetailView):    
    model = Product
    template_name = "home/product_detail.html"
    context_object_name = "product"
    slug_field = "slug"
    slug_url_kwarg = "slug"

class FaqView(TemplateView):
    template_name = "home/faq.html"