from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contnct(request):
    return render(request, 'website/contact.html')

def klic_course(request):
    return render(request, 'website/klic-course.html')

def mscit(request):
    return render(request, 'website/mscit.html')

# def courses(request):
#     return render(request, 'website/courses.html')