from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contnct, name='contact'),
    path('klic_course/', views.klic_course, name='klic_course'),
    path('mscit/', views.mscit, name='mscit'),
    path('klic/<int:klic_id>/',views.kilc_detail,name='detailpage')
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)