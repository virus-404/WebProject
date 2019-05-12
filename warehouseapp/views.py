<<<<<<< HEAD
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
=======
from django.shortcuts import render, get_object_or_404
>>>>>>> fc805fa1ae2b5932bc9e93d8679fae1568970c52
from django.db import models

from warehouseapp.forms import NewProductForm
from warehouseapp.models import Category
from warehouseapp.models.product import Product
from django.db.models import Q, F
from django import forms
from datetime import date
from .models import CatalogChange
from django.views.generic import ListView, DetailView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

<<<<<<< HEAD
from django.views.generic import ListView, TemplateView


=======
>>>>>>> fc805fa1ae2b5932bc9e93d8679fae1568970c52
# Create your views here.

def home_tecnic(request):
    context = {}
    context['title'] = 'Home-Tecnic'
    return render(request, 'warehouse/home-tecnic.html', context)


def home_comptatibilitat(request):
    context = {}
    context['title'] = 'Home-Comptabilitat'
    return render(request, 'magatzem/home-comptabilitat.html', context)

<<<<<<< HEAD

class HomeTecnicList(ListView):
=======
def delete_product(request, pk):
    template = 'warehouse/deleted-product.html'
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    CatalogChange.objects.get(product_id_change=product).delete()
    context = {}
    return render(request, template, context)

def update_product(request, pk):
    template = 'warehouse/update-product.html'
    context = {}
    Product.objects.filter(pk=pk).update(quantity=F('quantity')+request.GET.get('i'))
    CatalogChange.objects.create(product_id_change=Product.objects.get(pk=pk), category_id_change=Product.objects.get(pk=pk).category_id, quantity_modify=request.GET.get('i'), date=date.today())

    return render(request, template, context)

class HomeTecnicList(LoginRequiredMixin, ListView):
    login_url = ''
>>>>>>> fc805fa1ae2b5932bc9e93d8679fae1568970c52
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

class HomeComptabilitatList(LoginRequiredMixin, ListView):
    login_url = ''
    model = CatalogChange
    context_object_name = 'products'
    template_name = 'warehouse/home-comptabilitat.html'

    def get_queryset(self):
        return CatalogChange.objects.all()

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
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



