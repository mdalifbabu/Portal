from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Student(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    cgpa = models.FloatField(default=None)

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    credit = models.IntegerField(default=None)

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title