from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.views import generic
from django import forms
import openpyxl

from manager.uploader import UploadLogic
from manager.insert import InsertLogic

# Create your views here.

def index(request):
    return render(
        request,
        'shift/index.html',
    )

# Auto-Upload View
def auto_upload(request, uploader_name):
    form = None
    errors = []
    ers = []
    warnings = []
    returned = []
    responses = []
    valid = True

    uploaderMetadata = []
    uploaderMetadataParameters = []
    uploaderMetadataColumns = []

    uploaderMetadataLables = []
    uploaderMetadataParameterLabels = []
    uploaderMetadataColumnLabels = []
   
    # Get uploader metadata from database
    logic = UploadLogic
    ilogic = InsertLogic
    returned = logic.getUploaderMetadata(logic, uploader_name)
    uploaderMetadata = returned[0]
    valid = returned[1]
    ers = returned[2]
    for e in ers:
        errors.append(e)
    uploaderMetadataLabels = logic.getUploaderMetadataLabels(logic)
    if(uploaderMetadata):
        uploaderMetadata = zip(uploaderMetadataLabels, uploaderMetadata)

    # Get uploader metadata parameters from database
    if(valid):
        returned = logic.getUploaderMetadataParameters(logic, uploader_name)
        uploaderMetadataParameters = returned[0]
        valid = returned[1]
        ers = returned[2]
        for e in ers:
            errors.append(e)
        uploaderMetadataParameterLabels = logic.getUploaderMetadataParameterLabels(logic)

    # Get uploader metadata columns from database
    if(valid):
        returned = logic.getUploaderMetadataColumns(logic, uploader_name)
        uploaderMetadataColumns = returned[0]
        valid = returned[1]
        ers = returned[2]
        for e in ers:
            errors.append(e)
        uploaderMetadataColumnLabels = logic.getUploaderMetadataColumnLabels(logic)

    # Validate folder and file existence
    if(valid):
        returned = logic.validateFile(logic, uploader_name)
        valid = returned[1]
        ers = returned[2]
        for e in ers:
            errors.append(e)
    
    # Validate file metadata
    if(valid):
        inputFile = logic.getInputFile(logic, uploader_name)
        returned = logic.validateFileMetadata(logic, inputFile, uploader_name)
        valid = returned[1]
        ers = returned[2]
        for e in ers:
            errors.append(e)
        
        returned = ilogic.properInsert(logic, inputFile, uploader_name)


    return render(
        request,
        'shift/upload.html',
        {
            'form': form,
            'valid': valid,
            'responses': responses,
            'errors': errors,
            'warnings': warnings,
            'uploaderMetadata': uploaderMetadata,
            'uploaderMetadataParameters': uploaderMetadataParameters,
            'uploaderMetadataParameterLabels': uploaderMetadataParameterLabels,
            'uploaderMetadataColumns': uploaderMetadataColumns,
            'uploaderMetadataColumnLabels': uploaderMetadataColumnLabels,
        },
    )

# Manual Upload View
# TODO: REWORK BASED ON PARAMETERIZED CHANGES
def upload(request):
    # Submit File View
    if request.method == "POST" and request.POST.get('upload'):
        returned = []
        warnings = []
        form = UploadFileForm(request.POST, request.FILES)
        inputFile = request.FILES['file']
        if form.is_valid():
            logic = UploadLogic
            returned = logic.properInsert(logic,inputFile)
            responses = returned[0]
            warnings = returned[1]
            return render(
                request,
                'shift/index.html',
                {
                    'responses': responses,
                    'warnings': warnings
                },
            )
        else:
            responses.append('There was an error in uploading the file. Make sure to validate the file you uploaded.')
            return render(
                request,
                'shift/index.html',
                {
                    'responses': responses,
                    'warnings': warnings
                },
            )

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

