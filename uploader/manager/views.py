from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from . import views

def index(request):
    
    # TODO: Get all uploaders
    uploaders = ['shift', 'transition-countries']

    return render(
        request,
        'manager/index.html',
        {
            'uploaders': uploaders,
        },
    )