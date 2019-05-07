from django.shortcuts import render
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