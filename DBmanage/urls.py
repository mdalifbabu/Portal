from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portal-home'),
    path('teacher/', views.teacher, name='portal-teacher'),
    path('student/', views.student, name='portal-student'),
    path('course/', views.course, name='portal-course'),
    path('about/', views.about, name='portal-about'),
    
]
