from django.shortcuts import render
from .models import Klic_Course
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request,'madhuracomputer/index.html')

def about(request):
    return render(request, 'madhuracomputer/about.html')

def contnct(request):
    return render(request, 'madhuracomputer/contact.html')

def klic_course(request):
    klic=Klic_Course.objects.all()
    return render(request, 'madhuracomputer/klic-course.html',{'klic':klic})

def kilc_detail(request, klic_id):
    kcourse=get_object_or_404(Klic_Course,pk=klic_id)
    return render(request,'madhuracomputer/klic_detail.html',{'klic':kcourse})

def mscit(request):
    return render(request, 'madhuracomputer/mscit.html')
