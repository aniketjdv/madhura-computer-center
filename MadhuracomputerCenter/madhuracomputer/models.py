from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
class Klic_Course(models.Model):
    COURSE_TYPE_CHOICES=[
('AC',"Accounting Careers"),('BOC',"Back Office Careers"),('DC',"Designing Careers"),('DAC',"Digital Arts Careers"),('DF',"Digital Freelancing"),('FOC',"Front Office Careers"),('IHANC',"IT Hardware and Networking Careers"),('MNCJ',"Management New Collar Jobs"),('PC',"Programming Careers")
]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="kliccourse")
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=5,choices=COURSE_TYPE_CHOICES)
    description=models.TextField(default='')
    price=models.IntegerField(default=0)
    def __str__(self):
        return self.name