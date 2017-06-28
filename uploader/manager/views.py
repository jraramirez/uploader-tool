from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

def index(request):
    output = "Main Site"
    return HttpResponse(output)

def shift(request):
    return render(
        request,
        'shift/upload.html'
    )

def crosscharge(request):
    output = "Crosscharge Site"
    return render(
        request,
        'shift/upload.html'
    )