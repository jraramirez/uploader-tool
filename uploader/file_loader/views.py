from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.views import generic
from django import forms
from django.utils import timezone
import openpyxl
import datetime

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
    valid = True
    sendEmail = True
    truncate = False
    inputFile = None
    fileFullPath = None
    startTimeStamp = timezone.now()

    # TODO: use dictionary instead of lists
    errors = []
    ers = []
    warnings = []
    returned = []
    responses = []

    uploaderMetadata = []
    uploaderMetadataRaw = []
    # uploaderMetadataParameters = []
    uploaderMetadataColumns = []

    uploaderMetadataLables = []
    # uploaderMetadataParameterLabels = []
    uploaderMetadataColumnLabels = []
   
    # Get uploader metadata from database
    logic = UploadLogic
    ilogic = InsertLogic
    returned = logic.getUploaderMetadata(logic, uploader_name)
    uploaderMetadataRaw = returned[0]
    valid = returned[1]
    ers = returned[2]
    for e in ers:
        errors.append(e)
    uploaderMetadataLabels = logic.getUploaderMetadataLabels(logic)
    if(uploaderMetadataRaw):
        uploaderMetadata = zip(uploaderMetadataLabels, uploaderMetadataRaw)

    # Get uploader metadata parameters from database
    # if(valid):
    #     returned = logic.getUploaderMetadataParameters(logic, uploader_name)
    #     uploaderMetadataParameters = returned[0]
    #     valid = returned[1]
    #     ers = returned[2]
    #     for e in ers:
    #         errors.append(e)
    #     uploaderMetadataParameterLabels = logic.getUploaderMetadataParameterLabels(logic)

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
        returned = logic.validateFile(logic, uploaderMetadataRaw)
        valid = returned[1]
        ers = returned[2]
        sendEmail = returned[3]
        for e in ers:
            errors.append(e)
    
    # Validate file metadata
    if(valid):
        inputFile = logic.getInputFile(logic, uploaderMetadataRaw)
        fileFullPath = inputFile.name
        returned = logic.validateFileMetadata(logic, inputFile, uploaderMetadataRaw, uploaderMetadataColumns, 'auto')
        valid = returned[1]
        ers = returned[2]
        for e in ers:
            errors.append(e)

    # Insert after validations
    if(valid):
        returned = ilogic.properInsert(ilogic, inputFile, uploaderMetadataRaw, uploaderMetadataColumns, 'auto')
        valid = returned[1]
        ers = returned[2]
        for e in ers:
            errors.append(e)
        warnings = returned[3]

    # TODO: Decide when to truncate
    if(errors):
        truncate = True

    if(errors):
        responses.append("File upload have errors.")
    else:
        responses.append("File upload successful.")
    
    if(truncate):
        print("Truncated")
        ilogic.truncateTable(ilogic, uploaderMetadataRaw)

    # Move file after processing
    try:
        if(inputFile):
            inputFile.close()   
    except Exception:
        valid = False
        errors.append("The process cannot access the input file because it is being used by another process.")

    returned = logic.moveFile(logic, valid, uploaderMetadataRaw)
    valid = returned[1]
    ers = returned[2]
    for e in ers:
        errors.append(e)

    # Email all notifications
    if(sendEmail):
        elogic = EmailLogic 
        returned = elogic.sendEmailNotification(elogic, uploaderMetadataRaw, fileFullPath, valid, responses, errors, warnings)
        valid = returned[1]
        ers = returned[2]
        for e in ers:
            errors.append(e)

    # Insert log to log table
    if(sendEmail):
        returned = ilogic.insertLog(uploaderMetadataRaw, fileFullPath, errors, warnings, sendEmail, truncate, startTimeStamp, )

    return render(
        request,
        'file_loader/upload.html',
        {
            'form': form,
            'valid': valid,
            'responses': responses,
            'errors': errors,
            'warnings': warnings,
            'uploader_name': uploader_name,
            'uploaderMetadata': uploaderMetadata,
            # 'uploaderMetadataParameters': uploaderMetadataParameters,
            # 'uploaderMetadataParameterLabels': uploaderMetadataParameterLabels,
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
    inputFile = None

    uploaderMetadata = []
    uploaderMetadataRaw = []
    # uploaderMetadataParameters = []
    uploaderMetadataColumns = []

    uploaderMetadataLables = []
    # uploaderMetadataParameterLabels = []
    uploaderMetadataColumnLabels = []

    # Get uploader metadata from database
    logic = UploadLogic
    ilogic = InsertLogic
    returned = logic.getUploaderMetadata(logic, uploader_name)
    uploaderMetadataRaw = returned[0]
    valid = returned[1]
    ers = returned[2]
    for e in ers:
        errors.append(e)
    uploaderMetadataLabels = logic.getUploaderMetadataLabels(logic)
    if(uploaderMetadataRaw):
        uploaderMetadata = zip(uploaderMetadataLabels, uploaderMetadataRaw)

    # Get uploader metadata parameters from database
    # if(valid):
    #     returned = logic.getUploaderMetadataParameters(logic, uploader_name)
    #     uploaderMetadataParameters = returned[0]
    #     valid = returned[1]
    #     ers = returned[2]
    #     for e in ers:
    #         errors.append(e)
    #     uploaderMetadataParameterLabels = logic.getUploaderMetadataParameterLabels(logic)

    # Get uploader metadata columns from database
    if(valid):
        returned = logic.getUploaderMetadataColumns(logic, uploader_name)
        uploaderMetadataColumns = returned[0]
        valid = returned[1]
        ers = returned[2]
        for e in ers:
            errors.append(e)
        uploaderMetadataColumnLabels = logic.getUploaderMetadataColumnLabels(logic)

    # Submit File View
    if request.method == "POST" and request.POST.get('upload'):
        form = UploadFileForm(request.POST, request.FILES)
        inputFile = request.FILES['file']
        if form.is_valid():
            if(valid):
                inputFile = request.FILES['file']
                returned = logic.validateFileMetadata(logic, inputFile, uploaderMetadataRaw, uploaderMetadataColumns, 'assisted')
                valid = returned[1]
                ers = returned[2]
                for e in ers:
                    errors.append(e)
                if(valid):
                    returned = ilogic.properInsert(ilogic, inputFile, uploaderMetadataRaw, uploaderMetadataColumns, 'assisted')
                    valid = returned[1]
                    ers = returned[2]
                    for e in ers:
                        errors.append(e)
                    warnings = returned[3]
        else:
            errors.append('There was an error in uploading the file. Make sure that the file has passed validation.')
        if(valid and warnings):
            responses.append("File upload successful with warnings")
        elif(valid and not warnings):
            responses.append("File upload successful.")
        else:
            responses.append("File upload have errors.")
            # TODO: Truncate using the truncate variable
            ilogic.truncateTable(ilogic, uploaderMetadataRaw)
        try:       
            if(inputFile):
                inputFile.close()
        except Exception:
            valid = False
            errors.append("The process cannot access the input file because it is being used by another process.")

    # Validate File
    elif(request.method == "POST" and request.POST.get('validate metadata')):    
        # Validate file metadata
        form = UploadFileForm(request.POST, request.FILES)
        inputFile = request.FILES['file']
        returned = logic.validateFileMetadata(logic, inputFile, uploaderMetadataRaw, uploaderMetadataColumns, 'assisted')
        valid = returned[1]
        ers = returned[2]
        for e in ers:
            errors.append(e)
        if(valid):
            responses.append("Metadata is valid.")
        
        try:
            if(inputFile):
                inputFile.close()
        except Exception:
            valid = False
            errors.append("The process cannot access the input file because it is being used by another process.")

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
            'uploader_name': uploader_name,
            'uploaderMetadata': uploaderMetadata,
            # 'uploaderMetadataParameters': uploaderMetadataParameters,
            # 'uploaderMetadataParameterLabels': uploaderMetadataParameterLabels,
            'uploaderMetadataColumns': uploaderMetadataColumns,
            'uploaderMetadataColumnLabels': uploaderMetadataColumnLabels,
        },
    )
