from django import forms
from .models import Klic_Course

class Klic_course_form(forms.Form):
    klic_course_type=forms.ModelChoiceField(queryset=Klic_Course.objects.all(),label="select klic course type")