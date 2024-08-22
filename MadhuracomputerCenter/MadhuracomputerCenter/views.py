from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contnct(request):
    return render(request, 'website/contact.html')

def courses(request):
    return render(request, 'website/courses.html')