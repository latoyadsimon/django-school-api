from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    student_email = models.EmailField(max_length=255)
    personal_email = models.EmailField(max_length=255)
    locker_number = models.PositiveIntegerField()
    locker_combination = models.TextField()
    good_student = models.BooleanField()
    