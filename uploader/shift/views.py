from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.views import generic
from django import forms
import openpyxl

from manager.uploader import UploadLogic


class UploadFileForm(forms.Form):
    file = forms.FileField()

def index(request):
    output = "Shift Upload"
    return HttpResponse(output)

# Upload View
def upload(request):
    # Submit File View
    if request.method == "POST" and request.POST.get('upload'):
        form = UploadFileForm(request.POST, request.FILES)
        inputFile = request.FILES['file']
        if form.is_valid():
            # UploadLogic.properInsert(inputFile)
            return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()

    # Validate File
    elif(request.method == "POST" and request.POST.get('validate metadata')):
        errors = []
        valid = False

        uploaderMetadata = []
        uploaderMetadataParameters = []
        uploaderMetadataColumns = []

        uploaderMetadataLables = []
        uploaderMetadataParameterLabels = []
        uploaderMetadataColumnLabels = []

        form = UploadFileForm(request.POST, request.FILES)
        inputFile = request.FILES['file']

        # Get uploader metadata parameters and columns from database
        logic = UploadLogic
        uploaderMetadata = logic.getUploaderMetadata(logic)
        uploaderMetadataParameters = logic.getUploaderMetadataParameters(logic)
        uploaderMetadataColumns = logic.getUploaderMetadataColumns(logic)

        uploaderMetadataLabels = logic.getUploaderMetadataLabels(logic)
        uploaderMetadataParameterLabels = logic.getUploaderMetadataParameterLabels(logic)
        uploaderMetadataColumnLabels = logic.getUploaderMetadataColumnLabels(logic)

        if(uploaderMetadata):
            uploaderMetadata = zip(uploaderMetadataLabels, uploaderMetadata)

        # Validate after obtaining all the metadata
        
        errors = logic.validateFileMetadata(logic, inputFile)
        valid = errors[0]
        if(len(errors) > 1):
            errors = errors[1:len(errors)]
        else:
            errors = []
        return render(
            request,
            'shift/upload.html',
            {
                'form': form,
                'valid': valid,
                'errors': errors,
                'uploaderMetadata': uploaderMetadata,
                'uploaderMetadataParameters': uploaderMetadataParameters,
                'uploaderMetadataParameterLabels': uploaderMetadataParameterLabels,
                'uploaderMetadataColumns': uploaderMetadataColumns,
                'uploaderMetadataColumnLabels': uploaderMetadataColumnLabels,
            })

    # Default View
    else:
        form = UploadFileForm()
        uploaderMetadata = []
        uploaderMetadataParameters = []
        uploaderMetadataColumns = []

        uploaderMetadataLables = []
        uploaderMetadataParameterLabels = []
        uploaderMetadataColumnLabels = []

        # Get uploader metadata parameters and columns from database
        logic = UploadLogic
        uploaderMetadata = logic.getUploaderMetadata(logic)
        uploaderMetadataParameters = logic.getUploaderMetadataParameters(logic)
        uploaderMetadataColumns = logic.getUploaderMetadataColumns(logic)

        uploaderMetadataLabels = logic.getUploaderMetadataLabels(logic)
        uploaderMetadataParameterLabels = logic.getUploaderMetadataParameterLabels(logic)
        uploaderMetadataColumnLabels = logic.getUploaderMetadataColumnLabels(logic)
        
        if(uploaderMetadata):
            uploaderMetadata = zip(uploaderMetadataLabels, uploaderMetadata)
        
        return render(
            request,
            'shift/upload.html',
            {
                'form': form,
                'valid': False,
                'uploaderMetadata': uploaderMetadata,
                'uploaderMetadataParameters': uploaderMetadataParameters,
                'uploaderMetadataParameterLabels': uploaderMetadataParameterLabels,
                'uploaderMetadataColumns': uploaderMetadataColumns,
                'uploaderMetadataColumnLabels': uploaderMetadataColumnLabels,
            })

