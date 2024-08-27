from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'madhuracomputer/home.html')

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
