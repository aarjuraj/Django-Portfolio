from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def programmingprofile(request):
    return render(request, 'programmingprofile.html')


def webdevelopment(request):
    return render(request, 'web.html')
