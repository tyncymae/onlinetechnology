from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def indexView(request):
    return render(request, 'index.html')

def registerPage(request):
    form = CreateUserform()

    if request.method == 'POST':
        form = CreateUserform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'adamson/register.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Username OR password is incorrect')

    context = {}
    return render(request, 'adamson/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')