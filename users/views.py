from django.http import Http404
from django.shortcuts import redirect

# Create your views here.


def redirect_view(request):
    if request.user.groups.filter(name='Productor').exists():
        response = redirect('tecnic-home')
    elif request.user.groups.filter(name='Tecnic').exists():
        response = redirect('tecnic-home')
    elif request.user.groups.filter(name='Contabilitat').exists():
        response = redirect('contabilitat-home')
    elif request.user.groups.filter(name='Ceo').exists():
        response = redirect('ceo-home')
    else:
        raise Http404
    return response
