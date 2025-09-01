from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
# Create your views here.




class HomeView(TemplateView):
    template_name = "home/home.html"

class AboutView(TemplateView):
    template_name = "home/about.html"