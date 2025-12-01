from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import Product,Category
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    def get_queryset(self):
        if self.kwargs.get("slug"):
            return Product.objects.filter(category__slug=self.kwargs["slug"])
        return Product.objects.all()
    
    @method_decorator(cache_page(60 * 15 , key_prefix="products"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class ProductDetailView(DetailView):    
    model = Product
    template_name = "home/product_detail.html"
    context_object_name = "product"


class FaqView(TemplateView):
    template_name = "home/faq.html"