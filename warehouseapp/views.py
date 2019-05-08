from django.shortcuts import render

from warehouseapp.models import product
from django.db.models import Q
from django import forms

# import ListView (IMPORTA LIST VIEW)
# Create your views here.

def home_tecnic(request):
    context = {}
    context['title'] = 'Home-Tecnic'
    return render(request, 'warehouse/home-tecnic.html', context)

#mostrar tots els objectes de les bases de dades
# class ChangesListView(ListView):
# AQUI LA VIEW

def home_comptatibilitat(request):
    context = {}
    context['title'] = 'Home-Comptabilitat'
    return render(request, 'magatzem/home-comptabilitat.html', context)

def view_cards_products(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        items = Product.objects.filter(model_icontains = q)
        return render(request, 'warehouse/view-cards-products.html',{'items':items, 'query': Q})

    else:
        return HttpResponse('Please submit a search term.')
