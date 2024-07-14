from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm
from .models import User
from django.conf import settings


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('/')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        print(f"Form is valid: {form.is_valid()}")
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(f"Authenticated user: {user}")
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                print("Invalid user")
                print(f"Form errors: {form.errors}")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def main(request):
    return render(request, 'main.html')

def difficulty(request):
    return render(request, 'difficulty.html')

def sound(request):
    return render(request, 'sound.html')

def text(request):
    return render(request, 'text.html')

def themes(request):
    return render(request, 'themes.html')

def difficulty_level(request, level):
    return render(request, 'difficulty_level.html', {'level': level})

def theme_selection(request, theme):
    return render(request, 'theme_selection.html', {'theme': theme})
