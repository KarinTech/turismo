from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = "index.html"

class BarilochePage(TemplateView):
    template_name = "bariloche.html"

class CarlosPazPage(TemplateView):
    template_name = "carlospaz.html"

class SaltaPage(TemplateView):
    template_name = "salta.html"



