
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404

from django.db import models

from warehouseapp.forms import NewProductForm
from warehouseapp.models.product import Product
from django.db.models import Q, F
from django import forms
from datetime import date
from .models import CatalogChange, Category
from django.views.generic import ListView, DetailView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import ListView, TemplateView



# Create your views here.

def home_tecnic(request):
    context = {}
    context['title'] = 'Home-Tecnic'

    categories = Category.objects.get(category=Category)


    disc_dur_category = Category.filter(category="Disc dur")
    font_alimentacio_category = Category.filter(category="Font alimentacio")
    placa_base_category = Category.filter(category="Placa base")
    ssd_category = Category.filter(category="Memoria SSD")
    ram_category = Category.filter(category="Memoria RAM")
    microprocessador_category = Category.filter(category="Microprocessador")

    return render(request, 'warehouse/home-tecnic.html', context)


def home_comptatibilitat(request):
    context = {}
    context['title'] = 'Home-Comptabilitat'
    return render(request, 'magatzem/home-comptabilitat.html', context)




def delete_product(request, pk):
    template = 'warehouse/deleted-product.html'
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    CatalogChange.objects.filter(product_id_change=product).delete()
    context = {}
    return render(request, template, context)

def update_product(request, pk, counter):
    template = 'warehouse/update-product.html'
    context = {}
    change = 'i_'+str(counter)
    change_to_apply= int(request.GET.get(change))
    Product.objects.filter(pk=pk).update(quantity=F('quantity') + change_to_apply)
    product_to_change= Product.objects.get(pk=pk)
    nani = CatalogChange.objects.get_or_create(product_id_change=product_to_change, category_id_change=product_to_change.category_id, quantity_modify=change_to_apply, date=date.today())

    return render(request, template, context)


def search_product(request):
    template = 'warehouse/search-google.html'
    context={}
    return render(request, template, context)


class HomeTecnicList(LoginRequiredMixin, ListView):
    login_url = ''

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
class HomeCEOList(LoginRequiredMixin, ListView):
    login_url = ''

    model = Product
    context_object_name = 'items'
    template_name = 'warehouse/home-CEO.html'

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


class HomeComptabilitatList(LoginRequiredMixin, ListView):
    login_url = ''
    model = CatalogChange
    context_object_name = 'items'
    template_name = 'warehouse/home-comptabilitat.html'

    def get_queryset(self):
        return CatalogChange.objects.all()

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = 'CatalogChanges'
        return context
class ComptabilitatCEOList(LoginRequiredMixin, ListView):
    login_url = ''
    model = CatalogChange
    context_object_name = 'items'
    template_name = 'warehouse/comptabilitat.html'

    def get_queryset(self):
        return CatalogChange.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'CatalogChanges'
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

def home_proveidors(request):
    context = {}
    context['title'] = 'Home-CEO'
    return render(request, 'warehouse/home-CEO.html', context)

