from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        return
    return render (request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Emails is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,
                    email=email,password=password, username=username)
                    user.save()
                    messages.success(request, 'Registration successful, proceed to Login')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords does not match')
            return redirect('register')
    return render (request, 'accounts/register.html')

def logout(request):
    return redirect ('index')

def dashboard(request):
    return render (request, 'accounts/dashboard.html')