"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from warehouseapp.views import HomeTecnicList, HomeComptabilitatList, NewProductView, HomeCEOList, ComptabilitatCEOList
from django.urls import path, include
from . import views

urlpatterns = [
    path('tecnic/', HomeTecnicList.as_view(), name='tecnic-home'),
    path('deleted/<int:pk>', views.delete_product, name='deleted-product'),
    path('modify/<int:pk>/<int:counter>', views.update_product, name='update-product'),
    path('search/', views.search_product, name='search-google'),
    path('comptabilitat/', HomeComptabilitatList.as_view(), name='comptabilitat-home'),
    path('CEO/', HomeCEOList.as_view(), name='ceo-home'),
    path('CEO/comptabilitat', ComptabilitatCEOList.as_view(), name='ceo-comptabilitat'),
    path('new_product/', NewProductView.as_view(), name='new_product_form'),
]
