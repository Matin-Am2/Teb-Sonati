from django.urls import path,re_path
from . import views




app_name = "home"
urlpatterns = [
    path("home/",views.HomeView.as_view(),name="home"),
    path("about/",views.AboutView.as_view(),name="about"),
    path("products/",views.ProductsView.as_view(),name="products"),
    re_path(r"^products/(?P<slug>[\w\-\u0600-\u06FF]+)/$", views.ProductsView.as_view(), name="products2"),
    path("product/<int:pk>/",views.ProductDetailView.as_view(),name="product_detail"),
    path("faq/",views.FaqView.as_view(),name="faq")
]
