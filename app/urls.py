
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('Login/', views.Login, name='Login'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('create_post/', views.create_post, name='create_post'),
]
