from django.shortcuts import render,HttpResponse
from django.core.files.storage import FileSystemStorage
import os

from django.conf import settings
# Create your views here.

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

import subprocess

def run_stat(request, filename):
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    output = subprocess.check_output(['stat', filepath])
    return HttpResponse("Hello !!!")