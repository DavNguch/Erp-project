from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/wrong_login')
    else:
        return render(request,'index.html')

def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password2 = request.POST['password2']
        
        if password==password2:
            if User.objects.filter(username=username).exists():
                print('Username taken')
                messages.info(request,'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                print('Email taken')
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email= email)
                user.save();
                print('user created')
                messages.info(request,'User Created')
                return redirect('/')
        else:
            print('password not matching...')
            messages.info(request,'Password not matching')  
            return redirect('signup') 

    else:
        return render(request,'signup.html')

def wrong_login(request):
    return render(request,'wrong_login.html')

def help(request):
    return render(request,'help.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def user_detail(request):
    user = get_user_model()
    user.objects.all()
    guys = User.objects.all()
    return render(request,'user_detail.html', { 'guys': guys })
