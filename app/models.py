from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    username = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE)
    profileimage = models.ImageField(default='media/default_image.jpg.jpg', upload_to='media/profile_photos/')
    fullname = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    enroll_year = models.IntegerField()
    current_GPA = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

  
    def __str__(self):
        return f" {self.fullname} '--' {self.student_id}"

