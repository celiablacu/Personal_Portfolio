from django.shortcuts import render
from django.http import HttpResponse
import random
from django.shortcuts import redirect
# Create your views here.

def home(request):
    #return HttpResponse('Hello there')

    #render - function from Django that allows you to pass back
    #a template that turns evetually into an HTTP HttpResponse
    return render(request,'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+-=?'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length = int(request.GET.get('length','12'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')

def back(request):
    previous = request.POST.get('previous', '/')
    return redirect(previous)
