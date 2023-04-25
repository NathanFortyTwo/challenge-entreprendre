from django.shortcuts import render,HttpResponse
from django.core.files.storage import FileSystemStorage
import os

from django.conf import settings
from os import system

def homepage(request):
    context = {}
    return render(request,"homepage.html",context)


def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        return render(request, 'upload_file.html', {'message': 'File uploaded successfully.'})
    return render(request, 'upload_file.html')

def run_stat(request, filename):
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    system("stat "+filepath + ">output.txt")

    with open("output.txt") as f:
        data = f.read()
    
    system("rm "+filepath)


    return HttpResponse(data)