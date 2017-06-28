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
            UploadLogic.properInsert(inputFile)
            return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()

    # Validate File
    elif(request.method == "POST" and request.POST.get('validate metadata')):
        contents = []
        errors = []
        metadata = []
        fileMetadata = []

        form = UploadFileForm(request.POST, request.FILES)
        inputFile = request.FILES['file']

        # Get metadata from database
        labels = UploadLogic.getLabels()
        contents = UploadLogic.getMetadata()
        if(contents and labels):
            metadata = zip(labels, contents)    

        # Get metadata of input file
        contents = []
        contents = UploadLogic.readFileMetadata(inputFile)
        if(contents and labels):
            fileMetadata = zip(labels, contents)    

        errors = UploadLogic.validateFileMetadata(inputFile)
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
                'metadata': metadata,
                'fileMetadata': fileMetadata,
                'valid': valid,
                'errors': errors,
            })

    # Default View
    else:
        form = UploadFileForm()
        labels = []
        metadata =[]

        # Get metadata from database
        labels = UploadLogic.getLabels()
        contents = UploadLogic.getMetadata()
        if(contents and labels):
            metadata = zip(labels, contents)
        
        return render(
            request,
            'shift/upload.html',
            {
                'form': form,
                'valid': False,
                'metadata': metadata,
            })

def metadata_change(request):
    
    # Validate Metadata File
    if(request.method == "POST" and request.POST.get('validate new metadata')):
        contents = []
        changes = []
        fileMetadata = []
        metadata = []
        form = UploadFileForm(request.POST, request.FILES)
        inputFile = request.FILES['file']

        # Get metadata from database
        labels = UploadLogic.getLabels()
        contents = UploadLogic.getMetadata()
        if(contents and labels):
            metadata = zip(labels, contents)
        print(metadata)

        # Get metadata of input file
        contents = []
        contents = UploadLogic.readFileMetadata(inputFile)
        if(contents and labels):
            fileMetadata = zip(labels, contents)
        print(fileMetadata)

        # Get metadata changes
        changes = UploadLogic.getFileMetadataChanges(inputFile)
        hasChanges = changes[0]
        valid = changes[1]
        if(len(changes) > 2):
            changes = changes[2:len(changes)]
        else:
            changes = []
        return render(
            request,
            'shift/new-metadata.html',
            {
                'form': form,
                'metadata': metadata,
                'fileMetadata': fileMetadata,
                'valid': valid,
                'hasChanges': hasChanges,
                'changes': changes,
            })

    # Save File Metadata
    elif(request.method == "POST" and request.POST.get('save metadata changes')):
        contents = []
        metadata = []
        form = UploadFileForm(request.POST, request.FILES)
        inputFile = request.FILES['file']
        contents = UploadLogic.saveFileMetadata(inputFile)
        labels = UploadLogic.getLabels()
        if(contents and labels):
            metadata = zip(labels, contents)
        return render(
            request,
            'shift/new-metadata.html',
            {
                'form': form,
                'hasChanges': False,
                'metadata': metadata,
            })

    # Default View
    else:
        form = UploadFileForm()
        metadata = []

        # Get metadata from database
        labels = UploadLogic.getLabels()
        contents = UploadLogic.getMetadata()
        if(contents and labels):
            metadata = zip(labels, contents)
        return render(
            request,
            'shift/new-metadata.html',
            {
                'form': form,
                'valid': False,
                'hasChanges': False,
                'metadata': metadata,
            })


# class DetailView(generic.DetailView):
#     model = TestFIN005Raw
#     template_name = 'shift_upload/detail.html'


# class ResultsView(generic.DetailView):
#     model = TestFIN005Raw
#     template_name = 'shift_upload/results.html'


# def vote(request, question_id):
#     try:
#         query_result = "Response"
#         # question = get_object_or_404(TestFIN005Raw, pk=question_id)
#         context = {'query_result': query_result}
#     except TestFIN005Raw.DoesNotExist:
#         raise Http404("Does not exist")
#     return HttpResponseRedirect(reverse('shift_upload:results', args=(question_id,)))

# def index(request):
#     query_result = "Response"
#     context = {'query_result': query_result}
#     return render(request, 'shift_upload/index.html', context)

# def detail(request, question_id):
#     try:
#         query_result = "Response"
#         # question = get_object_or_404(TestFIN005Raw, pk=question_id)
#         context = {'query_result': query_result}
#     except TestFIN005Raw.DoesNotExist:
#         raise Http404("Does not exist")
#     return render(request, 'shift_upload/details.html', context)

# def results(request, question_id):
#     try:
#         query_result = "Response"
#         # question = get_object_or_404(TestFIN005Raw, pk=question_id)
#         context = {'query_result': query_result}
#     except TestFIN005Raw.DoesNotExist:
#         raise Http404("Does not exist")
#     return render(request, 'shift_upload/results.html', context)
