from django.contrib import admin

from .models import Profile, Post, Message, Event, Category


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'current_GPA', 'course', 'enroll_year')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','user',  'timestamp')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'reciever', 'timestamp')

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'date', 'time')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)