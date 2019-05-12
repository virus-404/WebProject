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
<<<<<<< HEAD
from warehouseapp.views import HomeTecnicList, NewProductView
=======
from warehouseapp.views import HomeTecnicList, HomeComptabilitatList
>>>>>>> fc805fa1ae2b5932bc9e93d8679fae1568970c52
from django.urls import path, include
from . import views

urlpatterns = [
    path('tecnic/', HomeTecnicList.as_view(), name='tecnic-home'),
    path('deleted/<int:pk>', views.delete_product, name='deleted-product'),
    path('modify/<int:pk>', views.update_product, name='update-product'),
    path('comptabilitat/', HomeComptabilitatList.as_view(), name='comptabilitat-home'),
    # path('CEO/', views.home_proveidors, name='comptabilitat-home'),
    path('new_product/', NewProductView.as_view(), name='new_product_form'),
]
