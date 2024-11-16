from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Post, Event, Message, Category, Profile

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
          'user_post': user_post,
    }
    return render(request, 'app/index.html', context)

@login_required(login_url='Login/')
def profile(request, user_id):
    

    # url = reverse('profile', kwargs={'user_id': user_profile.id})

    user_profile = get_object_or_404(Profile, id=user_id)

    return render(request, 'app/profile.html', {'user_profile':user_profile})
def register(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username):
                
                    messages.info(request, 'Account with {username} Already exist, Want to Retrieve Account?')
                    context = {
                        'username': username,
                    }
                    return redirect('register')
            elif User.objects.filter(email=email):
                    messages.info(request, 'Account with {email} Already exist, Want to Retrieve Account?')
                    context = {
                        'username': username,
                        'email': email,
                    }
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
        specialization = request.POST['specialization']
        
        if Profile.objects.filter(fullname=fullname):
              
              messages.info(request, 'account already exist with {fullname}')

              context = {
                   'fullname': fullname,
              }
              return redirect('onboarding')
        
        elif Profile.objects.filter(current_GPA=current_GPA):
                messages.info(request, 'user already exist with {current_GPA}')

                context = {
                   'fullname': fullname,
                   'current_GPA': current_GPA,
              }
                return redirect('onboarding', context)

        else:
            student_profile = Profile.objects.create(username=username,profileimage=profileimage, fullname=fullname, course=course, enroll_year=enroll_year, department=department, specialization=specialization)
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
            messages.info(request, 'User does not exist')
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

def chat_box(request):
     return render(request, 'app/messages.html')

     
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