from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    username = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    enroll_year = models.IntegerField()
    current_GPA = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

  
    def __str__(self):
        return self.fullname

