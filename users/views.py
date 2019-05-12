from django.http import Http404
from django.shortcuts import redirect

# Create your views here.


def redirect_view(request):
    if request.user.groups.filter(name='Proveidors').exists():
        response = redirect('tecnic-home')
    elif request.user.groups.filter(name='Tecnic').exists():
        response = redirect('tecnic-home')
    elif request.user.groups.filter(name='Comptabilitat').exists():
        response = redirect('comptabilitat-home')
    elif request.user.groups.filter(name='Ceo').exists():
        response = redirect('ceo-home')
    else:
        raise Http404
    return response
