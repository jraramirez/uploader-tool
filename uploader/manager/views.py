from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from . import views

def index(request):
    output = "Main Site"
    return render(
        request,
        'manager/index.html'
    )