from django.shortcuts import render
from .models import Teacher, Student, Course
from django.contrib.auth.models import User

def home(request):
    return render(request, 'portal/home.html')

def teacher(request):

    for d in Teacher.objects.all():
        date_posted = d.date_posted

    context = {
        'teachers' : Teacher.objects.all(),
        'date_posted' : date_posted,
        'title' : 'Teacher',
    }
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('id_number') and request.POST.get('phone_number') and request.POST.get('email'):
            th = Teacher()
            th.name = request.POST.get('name')
            th.id_number = request.POST.get('id_number')
            th.phone_number = request.POST.get('phone_number')
            th.email = request.POST.get('email')
            th.author = User.objects.filter(username='Alif').first()
            th.save()
            return render(request, 'portal/teacher.html', context)
    else:
        return render(request, 'portal/teacher.html', context) 

def student(request):

    for d in Student.objects.all():
        date_posted = d.date_posted

    context = {
        'students' : Student.objects.all(),
        'date_posted' : date_posted,
        'title' : 'Student',
    }
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('id_number') and request.POST.get('phone_number') and request.POST.get('email') and request.POST.get('cgpa'):
            st = Student()
            st.name = request.POST.get('name')
            st.id_number = request.POST.get('id_number')
            st.phone_number = request.POST.get('phone_number')
            st.email = request.POST.get('email')
            st.cgpa = request.POST.get('cgpa')
            st.author = User.objects.filter(username='Alif').first()
            st.save()
            return render(request, 'portal/student.html', context)
    else:
        return render(request, 'portal/student.html', context)

def course(request):

    for d in Course.objects.all():
        date_posted = d.date_posted

    context = {
        'courses' : Course.objects.all(),
        'date_posted' : date_posted,
        'title' : 'Course',
    }
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('code') and request.POST.get('credit'):
            cr = Course()
            cr.title = request.POST.get('title')
            cr.code = request.POST.get('code')
            cr.credit = request.POST.get('credit')
            cr.author = User.objects.filter(username='Alif').first()
            cr.save()
            return render(request, 'portal/course.html', context)
    else:
        return render(request, 'portal/course.html', context) 


def about(request):
    return render(request, 'portal/about.html', {'title' : 'About'})
