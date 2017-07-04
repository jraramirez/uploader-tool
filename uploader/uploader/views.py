from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

def index(request):
    return render(
        request,
        'manager/index.html',
    )