
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<uuid:user_id>/', views.profile, name='profile'),
    path('edit-profile/<uuid:user_id>/', views.edit_profile, name='edit-profile'),
    path('register/', views.register, name='register'),
    path('Login/', views.Login, name='Login'),
    path('Logout/', views.Logout, name='Logout'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('create_post/', views.create_post, name='create_post'),
    path('new_category/', views.new_category, name='new_category'),
    path('chat_list/', views.chat_list, name='chat_list'),
    path('chat_view/<str:receiver_id>/', views.chat_view, name='chat_view'),
    path('send-message/', views.send_message, name='send-message'),
    path('get-messages/<uuid:msg_id>/', views.get_messages, name='get-messages'),
    path('conversation/<uuid:msg_id>/', views.conversation, name='conversation'),
    path('error_404/', views.error_404, name='error_404'),
    path('new_event/', views.new_event, name='new_event'),
]
