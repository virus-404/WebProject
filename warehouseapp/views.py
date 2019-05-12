from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import models

from warehouseapp.forms import NewProductForm
from warehouseapp.models import Category
from warehouseapp.models.product import Product
from django.db.models import Q
from django import forms

from django.views.generic import ListView, TemplateView


# Create your views here.

def home_tecnic(request):
    context = {}
    context['title'] = 'Home-Tecnic'
    return render(request, 'warehouse/home-tecnic.html', context)


def home_comptatibilitat(request):
    context = {}
    context['title'] = 'Home-Comptabilitat'
    return render(request, 'magatzem/home-comptabilitat.html', context)


class HomeTecnicList(ListView):
    model = Product
    context_object_name = 'items'
    template_name = 'warehouse/home-tecnic.html'

    def get_queryset(self):
        if 'q' in self.request.GET and self.request.GET['q']:
            q = self.request.GET['q']
            items = Product.objects.filter(name__icontains=q)
            return items
        else:
            return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Productes'
        return context


class NewProductView(TemplateView):
    template_name = 'warehouse/new-product.html'

    def get(self, request):
        form = NewProductForm()
        categories = Category.category

        args = {'form': form, 'categories':categories}
        return render(request, self.template_name, args)

    def post(self, request):
        form = NewProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/warehouse/tecnic')

        return render(request, self.template_name, {'form':form})



