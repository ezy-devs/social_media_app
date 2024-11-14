from django.contrib import admin

from .models import Student, Post, Message, Event


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'current_GPA', 'course', 'enroll_year')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','user',  'timestamp')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'reciever', 'timestamp')

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'date', 'time')

admin.site.register(Student, StudentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Event, EventAdmin)