from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.


# class Student(models.Model):
#     username = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE)
#     profileimage = models.ImageField(default='media/default_image.jpg.jpg', upload_to='media/profile_photos/')
#     fullname = models.CharField(max_length=100)
#     student_id = models.CharField(max_length=100)
#     course = models.CharField(max_length=100)
#     enroll_year = models.IntegerField()
#     current_GPA = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
#     department = models.CharField(max_length=100)
#     specialization = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE)
    profileimage = models.ImageField(default='media/default_image.jpg', upload_to='profile_images/')
    fullname = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    enroll_year = models.IntegerField()
    current_GPA = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    student_id = models.CharField(max_length=100, default='')
  
class Category(models.Model):
    user = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)   


class Post(models.Model):
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name='reciever', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

   