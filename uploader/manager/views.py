from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from . import views

from manager.uploader import UploadLogic

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

def refresh(request):
    
    logic = UploadLogic

    # TODO: Get all uploaders
    uploaders = ['shift', 'transition-countries']

    data = logic.getAllTargetTablesAndSchemas(logic)['data']
    logic.putTargetTablesToModels(logic, data)

    return render(
        request,
        'manager/index.html',
        {
            'uploaders': uploaders,
        },
    )