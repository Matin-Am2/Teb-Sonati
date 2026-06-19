from django.urls import path,re_path
from django_distill import distill_path,distill_re_path
from .models import Product,Category
from . import views


app_name = "home"

def get_product_urls():
    for product in Product.objects.all():
        yield {"slug":product.slug}

def get_category_urls():
    for category in Category.objects.all():
        yield {"slug": category.slug}

urlpatterns = [


distill_re_path(
    r"^product/(?P<slug>[\w\-\u0600-\u06FF]+)/$",
    views.ProductDetailView.as_view(),
    name="product_detail",
    distill_func=get_product_urls,
),
distill_re_path(
    r"^products/(?P<slug>[\w\-\u0600-\u06FF]+)/$",
    views.ProductsView.as_view(),
    name="products2",
    distill_func=get_category_urls,
),

distill_path(
    "home/",
    views.HomeView.as_view(),
    name="home",
),

distill_path(
    "about/",
    views.AboutView.as_view(),
    name="about",
),

distill_path(
    "products/",
    views.ProductsView.as_view(),
    name="products",
),

distill_path(
    "faq/",
    views.FaqView.as_view(),
    name="faq",
),
]



# # urlpatterns = [
# #     path("home/",views.HomeView.as_view(),name="home"),
# #     path("about/",views.AboutView.as_view(),name="about"),
# #     path("products/",views.ProductsView.as_view(),name="products"),
# #     re_path(r"^products/(?P<slug>[\w\-\u0600-\u06FF]+)/$", views.ProductsView.as_view(), name="products2"),
# #     re_path(r"^product/(?P<slug>[-\w\u0600-\u06FF]+)/$",views.ProductDetailView.as_view(), name="product_detail", ),   
# #     path("faq/",views.FaqView.as_view(),name="faq")
# # ]
