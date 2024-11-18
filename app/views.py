from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import json
from .models import Post, Event, Message, Category, Profile, Conversation

from .forms import PostCreationForm

# Create your views here.

@login_required(login_url='Login/')
def home(request):
    posts = Post.objects.all()
    # user_post = Pr.objects.get(user=user_profile.username)
    # user_post = get_object_or_404(Profile, username=post)
    
    try: 
        user_profile = Profile.objects.get(username=request.user)      
    except:
            messages.info(request, 'Hi!, Update your Profile to continue enjoying this platform')
            return redirect('onboarding')
    context = {
         'user_profile': user_profile,
         'posts':posts,
        #   'user_post': user_post,
    }
    return render(request, 'app/index.html', context)

@login_required(login_url='Login/')
def profile(request, user_id):
    

    # url = reverse('profile', kwargs={'user_id': user_profile.id})

    user_profile = get_object_or_404(Profile, id=user_id)

    return render(request, 'app/profile.html', {'user_profile':user_profile})

def edit_profile(request, user_id):
     user_profile = Profile.objects.get(username=request.user)  

     return render(request, 'app/edit-profile.html', {'user_profile':user_profile})
def register(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                
                    messages.info(request, f'Account with {username} Already exist, try again')
                    
                    return redirect('register')
            elif User.objects.filter(email=email).exists():
                    messages.info(request, f'Account with {email} Already exist, try again')
                    
                    return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request, user)

                return redirect('onboarding')
            
        messages.info(request, 'password does not match, try again')
        
        context = {
                        'username': username,
                        'email': email,
                    }
        return redirect('register')

    else:
        return render(request, 'app/signup.html')
            
            
    return render(request, 'app/signup.html')


def onboarding(request):
    if request.method == 'POST':
        username = request.user
        profileimage = request.FILES.get('image')
        fullname = request.POST['fullname']
        course = request.POST['course']
        enroll_year = request.POST['enroll_year']
        current_GPA = request.POST['gpa']
        department = request.POST['department']
        student_id = request.POST['student_id']
        specialization = request.POST['specialization']
        
        if Profile.objects.filter(fullname=fullname):
              
              messages.info(request, 'account already exist with {fullname}')

              context = {
                   'fullname': fullname,
              }
              return redirect('onboarding')
        
        else:
            student_profile = Profile.objects.create(username=username, profileimage=profileimage, fullname=fullname, course=course, current_GPA=current_GPA, student_id=student_id, enroll_year=enroll_year, department=department, specialization=specialization)
            student_profile.save()
            messages.info(request, "Thanks You've Successfully Setup your Profile!")
            return redirect('/')
         
    return render(request, 'app/onboarding.html')

def Login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
           
            login(request, user)
            messages.info(request, f'{username} your are Logged in Successfully!')
            return redirect('home')
                   
        else:
            messages.info(request, 'Wrong Credentials, try again!')
            return redirect('Login')
        
    return render(request, 'app/Login.html')

def Logout(request):
     logout(request)
     return redirect('Login')

def create_post(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        user = request.user
        category_id = request.POST['category']
        content = request.POST['content']
        image = request.FILES.get('image')

        category = get_object_or_404(Category, id=category_id)
        new_post = Post.objects.create(user=user, category_id=category, content=content, image=image)
        new_post.save()

        context = {
              
         }
        return redirect('/')

    return render(request, 'app/create_post.html', {'categories':categories})

def chat_list(request):
    try: 
        user_profile = Profile.objects.get(username=request.user)      
    except:
            messages.info(request, 'Hi!, Update your Profile to continue enjoying this platform')
            return redirect('onboarding')
    context = {
         'user_profile': user_profile,
        #  'posts':posts,
        #   'user_post': user_post,
    }
    return render(request, 'app/chat-list.html', context)

def chat_view(request, receiver_id):
    receiver = User.objects.get(id=receiver_id)
    chats = Message.objects.filter(reciever=receiver, sender=request.user)
    sender_msg = Message.objects.filter(sender=request.user)
    receiver_msg = Message.objects.filter(reciever=receiver)
    try: 
        user_profile = Profile.objects.get(username=request.user)      
    except:
            messages.info(request, 'Hi!, Update your Profile to continue enjoying this platform')
            return redirect('onboarding')
    context = {
         'user_profile': user_profile,
        #  'posts':posts,
        #   'user_post': user_post,
        'receiver_id': receiver.id,
        'chats':chats,
        'sender_msg':sender_msg,
        'receiver_msg':receiver_msg,
    }
    # sender = request.user
    # message = Message.objects.get(sender=sender, reciever=receiver)
    # context = {
    #      'messages':message
    # }

    return render(request, 'app/chatbox.html', context)


def error_404(request):
     
     return render(request, 'app/404_error.html')

def conversation(request, msg_id):
    user_profile = Profile.objects.get(username=request.user)     
    try:  
        msg_id = Conversation.objects.get(id=msg_id)
        
    except:
     return redirect('error_404')

    return render(request, 'app/chatbox.html', {'user_profile':user_profile})
    
def get_messages(request, msg_id):
    user_profile = Profile.objects.get(username=request.user) 
    if request.method == 'GET':    
        try:  
            msg_id = Conversation.objects.get(id=msg_id)
        except:
            return redirect('error_404')
        

        return render(request, 'app/chatbox.html', {'user_profile':user_profile})
    
def send_message(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            sender = request.user
            receiver_id = data.get('receiver_id')
            content = data.get('content')

            receiver = get_object_or_404(User, id=receiver_id)
            message = Conversation.objects.create(sender=sender, receiver=receiver, content=content)
            
            return JsonResponse({'status': 'success', 'message_id': message.id})

def get_messages(request, msg_id):
     if request.method == 'GET':
        sender = request.user
        receiver =get_object_or_404(User, id=msg_id)
        message_list = Message.objects.filter(sender=sender, reciever=receiver) | Message.objects.filter(sender=receiver, reciever=sender)
        message_list.order_by('timestamp')
        return JsonResponse({'messages': list(message_list.values())})


# MANAGEMENT 
def new_category(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST['name']
        description = request.POST['description']
        
        if Category.objects.filter(name=name).exists():
             messages.info(request, 'Category with {name} already Exists')
             context = {
                  'name': name,
                  'description': description,
             }
             return redirect('new_category', context)

        category = Category.objects.create(user=user, name=name, description=description)
        category.save()

        context = {
            
        }
        return redirect('/', )
    return render(request, 'admin/new_category.html')

def new_event(request):
     return render(request, 'admin/new_event.html')