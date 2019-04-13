from django.shortcuts import render
# Create your views here.

def home_tecnic(request):
    context = {}
    context['title'] = 'Home-Tecnic'
    return render(request, 'warehouse/home-tecnic.html', context)


# def home_comptatibilitat(request):
    # context = {}
    # context['title'] = 'Home-Comptabilitat'
    # return render(request, 'magatzem/logers.html', context)