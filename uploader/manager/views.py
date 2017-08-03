from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from . import views

from manager.uploader import UploadLogic

def index(request):
    
    logic = UploadLogic

    # Get all uploader names
    returned = logic.getAllUploaderNames(logic)
    uploaders = returned['data']['names']

    return render(
        request,
        'manager/index.html',
        {
            'uploaders': uploaders,
        },
    )

def refresh(request):
    
    logic = UploadLogic

    # Get all uploader names
    returned = logic.getAllUploaderNames(logic)
    uploaders = returned['data']['names']

    data = logic.getAllTargetTablesAndSchemas(logic)['data']
    logic.putTargetTablesToModels(logic, data)

    return render(
        request,
        'manager/index.html',
        {
            'uploaders': uploaders,
        },
    )