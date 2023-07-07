from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

def index(request):
    return render(request, 'index.html')

def bariloche(request):
    return render(request, 'bariloche.html')

def salta(request):
    return render(request, 'salta.html')

def carlospaz(request):
    return render(request, 'carlospaz.html')

#class IndexView(TemplateView):
    #template_name = "index.html"

#class BarilochePage(TemplateView):
    #template_name = "bariloche.html"

#class CarlosPazPage(TemplateView):
    #template_name = "carlospaz.html"

#class SaltaPage(TemplateView):
    #template_name = "salta.html"

def index(request):
    return render(request, 'index.html')

def bariloche(request):
    return render(request, 'bariloche.html')

def salta(request):
    return render(request, 'salta.html')

def carlospaz(request):
    return render(request, 'carlospaz.html')

