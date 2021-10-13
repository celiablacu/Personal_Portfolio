from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request,'portfolio/home.html', {'projects':projects})

def back(request):
    previous = request.POST.get('previous', '/')
    return redirect(previous)

def horses(request):
    return render(request,'portfolio/horses.html')

def dogs(request):
    return render(request,'portfolio/dogs.html')

def cats(request):
    return render(request,'portfolio/cats.html')

def rescues(request):
    return render(request,'portfolio/rescues.html')

def projects(request):
    return render(request,'portfolio/projects.html')
