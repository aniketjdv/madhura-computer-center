from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
class Klic_Course(models.Model):
    COURSE_TYPE_CHOICES=[
"Accounting Careers","Back Office Careers","Designing Careers","Digital Arts Careers","Digital Freelancing","Front Office Careers","IT Hardware and Networking Careers","Management New Collar Jobs","Programming Careers"
]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="/klic_course")
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(choices=COURSE_TYPE_CHOICES)
    desc=models.TextField()