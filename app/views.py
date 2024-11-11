from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Student


# Create your views here.


def home(request):
    return render(request, 'app/index.html')


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
                    return redirect('register', context)
            elif User.objects.filter(email=email):
                    messages.info(request, 'Account with {email} Already exist, Want to Retrieve Account?')
                    context = {
                        'username': username,
                        'email': email,
                    }
                    return redirect('register', context)
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('onboarding')
            
        messages.info(request, 'password does not match, try again')
        context = {
                        'username': username,
                        'email': email,
                    }
        return redirect('register', context)

    else:
        return render(request, 'app/signup.html')
            
            
    return render(request, 'app/signup.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, '{username} your are Logged in Successfully!')
            
            return redirect('/', {'messages':messages})
        else:
            messages.info(request, 'User does not exist')

            context = {
                'username':username,
            }
            return redirect('Login', context)
    return render(request, 'app/Login.html')

def onboarding(request):
    if request.method == 'POST':
        username = request.user
        fullname = request.POST['fullname']
        studentId = request.POST['studentId']
        course = request.POST['course']
        enroll_year = request.POST['enroll_year']
        current_GPA = request.POST['gpa']
        department = request.POST['department']
        specialization = request.POST['specialization']

        if Student.objects.filter(fullname=fullname):
              messages.info(request, 'account already exist with {fullname}')

              context = {
                   'fullname': fullname,
              }
              return redirect('onboarding', context)
        elif Student.objects.filter(current_GPA=current_GPA):
                messages.info(request, 'user already exist with {current_GPA}')

                context = {
                   'fullname': fullname,
                   'current_GPA': current_GPA,
              }
                return redirect('onboarding', context)

        else:
            student_profile = Student.objects.create(username=username, fullname=fullname, studentId=studentId, course=course, enroll_year=enroll_year, department=department, specialization=specialization)
            student_profile.save()
            success_msg = ""
            return redirect('/')
         
    return render(request, 'app/onboarding.html')



def create_post(request):
    return render(request, 'app/create_post.html')