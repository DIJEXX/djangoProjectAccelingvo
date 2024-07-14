from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.conf import settings
from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required


# - Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")


    context = {'registerform':form}

    return render(request, 'register.html', context=context)



def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("main")


    context = {'loginform':form}

    return render(request, 'login.html', context=context)
def main(request):
    return render(request, 'main.html')

# def login(request):
#     return render(request, 'login.html')

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