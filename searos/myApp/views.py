from django.shortcuts import render,HttpResponse
from django.core.files.storage import FileSystemStorage
import os

from django.conf import settings
from os import system
from time import sleep



def index(request):
    context = {}
    return render(request,"index.html",context)

def about(request):
    context = {}
    return render(request,"about.html",context)


def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        return render(request, 'upload_code.html', {'message': 'File uploaded successfully.'})
    return render(request, 'upload_code.html')



def run_stat(request, filename):
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    init = "docker start seahorn_web"
    command = f"docker exec seahorn_web sea pf -m64 /host/{filename} | tail -n 1 > output_sea.txt"
    #create = f"docker run  --name=seahorn_web -v {settings.BASE_DIR}/MEDIA:/host seahorn/seahorn-llvm5"
    #system(create)
    system(init)
    sleep(3)
    system(command)

    with open("output_sea.txt") as f:
        data = f.read()
    
    system("rm "+filepath)
    system("docker stop seahorn_web")
    return HttpResponse(data)