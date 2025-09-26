from django.urls import path
from . import views




app_name = "home"
urlpatterns = [
    path("home/",views.HomeView.as_view(),name="home"),
    path("about/",views.AboutView.as_view(),name="about"),
    path("products/",views.ProductsView.as_view(),name="products"),
    path("product/<int:pk>/",views.ProductDetailView.as_view(),name="product_detail")
]
