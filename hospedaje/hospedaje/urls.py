"""
URL configuration for hospedaje project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django import render
from .views import views
from .views import views 
from .views import bariloche
from .views import carlospaz
from .views import salta 




#urlpatterns = [

    #path('admin/', admin.site.urls),
    #path('', IndexView.as_view(), name="index"),
    #path("bariloche", BarilochePage.as_view(), name="bariloche"),    
    #path("carlospaz", CarlosPazPage.as_view(), name="carlospaz"), 
    #path("salta", SaltaPage.as_view(), name="salta")]
    
urlpatterns =[
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('bariloche', views.bariloche, name='bariloche'),
    path('salta', views.salta, name='salta'),
    path('carlospaz', views.carlospaz, name='carlospaz'),]