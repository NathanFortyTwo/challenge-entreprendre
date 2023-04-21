from django.shortcuts import render

# Create your views here.

def homepage(request):
    context = {}
    return render(request,"homepage.html",context)


def get_started(request):
    context = {}
    return render(request,"get_started.html",context)