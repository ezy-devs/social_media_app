
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<uuid:user_id>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('Login/', views.Login, name='Login'),
    path('Logout/', views.Logout, name='Logout'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('create_post/', views.create_post, name='create_post'),
    path('new_category/', views.new_category, name='new_category'),
    path('chat_box/', views.chat_box, name='chat_box'),
    path('new_event/', views.new_event, name='new_event'),
]
