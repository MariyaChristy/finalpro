from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from MovieApp.forms import RegistrationForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        userName=request.POST['username']
        passWord=request.POST['password']
        user=auth.authenticate(username=userName,password=passWord)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('credentials_app:login')

    messages.success(request,'registration is success')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('credentials_app:login')  # Redirect to your home page or another desired URL
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')