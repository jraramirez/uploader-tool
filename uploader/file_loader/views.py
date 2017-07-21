from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.views import generic
from django import forms
import openpyxl

from manager.uploader import UploadLogic
from manager.insert import InsertLogic
from manager.email import EmailLogic

class UploadFileForm(forms.Form):
    file = forms.FileField()

def index(request):
    return render(
        request,
        'file_loader/index.html',
    )

# Auto-Upload View
def auto_upload(request, uploader_name):
    form = None
    errors = []
    ers = []
    warnings = []
    # TODO: use dictionary instead of lists
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
        if(valid):
            responses.append("File is valid.")
        else:
            responses.append("File is not valid.")

    # # Insert after validations
    if(valid):
        returned = ilogic.properInsert(ilogic, inputFile, uploader_name)
        valid = returned[1]
        ers = returned[2]
        for e in ers:
            errors.append(e)
        responses = returned[3]
        warnings = returned[4]
    
    # Move file after processing
    returned = logic.moveFile(logic, valid, uploaderMetadata)
    valid = returned[1]
    ers = returned[2]
    for e in ers:
        errors.append(e)

    # Email all notifications
    # TODO: Get sender and recipient from metadata table
    # elogic = EmailLogic
    # sender = "pg_bizopssupport@hpe.com"
    # recipient = "joe-ramir.agn.ramirez@hpe.com"
    # elogic.sendEmailNotification(
    #     elogic,
    #     sender,
    #     recipient,
    #     valid,
    #     responses,
    #     errors,
    #     warnings,
    #     uploader_name
    # )

    return render(
        request,
        'file_loader/upload.html',
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
def upload(request, uploader_name):

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

    # Submit File View
    if request.method == "POST" and request.POST.get('upload'):
        form = UploadFileForm(request.POST, request.FILES)
        inputFile = request.FILES['file']
        if form.is_valid():
            ilogic = InsertLogic
            returned = ilogic.properInsert(ilogic, inputFile, uploader_name)
            valid = returned[1]
            ers = returned[2]
            for e in ers:
                errors.append(e)
            responses = returned[3]
            warnings = returned[4]
        else:
            errors.append('There was an error in uploading the file. Make sure that the file has passed validation.')

    # Validate File
    elif(request.method == "POST" and request.POST.get('validate metadata')):    
        # Validate file metadata
        form = UploadFileForm(request.POST, request.FILES)
        inputFile = request.FILES['file']
        returned = logic.validateFileMetadata(logic, inputFile, uploader_name)
        valid = returned[1]
        ers = returned[2]
        for e in ers:
            errors.append(e)
        if(valid):
            responses.append("File is valid.")

    # Default View
    else:
        form = UploadFileForm()
    
    return render(
        request,
        'file_loader/upload.html',
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
