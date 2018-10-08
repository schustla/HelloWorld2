from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .forms import UploadFileForm
import pandas as pd

def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def upload_file(request):
    if request.method == 'POST':
        excel_file = request.FILES["excel_file"]
        pd_in = pd.read_excel(excel_file)
        #if form.is_valid():
           # handle_uploaded_file(request.FILES['file'])
            #return HttpResponseRedirect('/success/url/')
        print(pd_in)

        context_out = {
            'ncol': pd_in.columns.size,
            'excel_file': "上传"
        }
    else:
        excel_file = UploadFileForm()
        context_out = {
           'ncol': "2",
           'excel_file': "上传"
        }
    return render(request, 'upload.html',context=context_out)

def handle_uploaded_file(f):
    with open('some/file/name.excel', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

