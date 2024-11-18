from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile, Post, Message, Event, Category, Conversation


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

class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'timestamp')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Conversation, ConversationAdmin)
