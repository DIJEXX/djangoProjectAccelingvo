from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, RegistrationFormEng, LoginForm
from .models import User
from django.conf import settings


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # login_form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.language = 'ru'
            user.save()
            return redirect('/')
        # elif login_form.is_valid():
        #     user = login_form.get_user()
        #     login(request, user)
        #     return redirect('/')
    else:
        form = RegistrationForm()
        # login_form = LoginForm()
    return render(request, 'register.html', {'form': form})
    # return render(request, 'register.html', {'form': form, 'login_form': login_form})

def register_eng(request):
    if request.method == 'POST':
        form = RegistrationFormEng(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.language = 'en'
            user.save()
            return redirect('/')
    else:
        form = RegistrationFormEng()
    return render(request, 'register_eng.html', {'form': form})


# def login(request):
#     print("Login")
#     if request.method == 'POST':
#
#         form = LoginForm(request, data=request.POST)
#         print(form.get_user())
#
#         if form.is_valid():
#             user = form.get_user()
#             print(user)
#             login(request, user)
#             return redirect('main')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})
#     # return render(request, 'login.html', {'login_form': form})

def login(request):
    print("Login")
    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)
        print(form.get_user())
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        print(user)
        login(request, user)
        return redirect('main')
        # if form.is_valid():
        #     user = authenticate(
        #         username=request.POST.get('username'),
        #         password=request.POST.get('password')
        #     )
        #     print(request.POST.get('username'))
        #     print(request.POST.get('password'))
        #     print(user)
        #     login(request, user)
        #     return redirect('main')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    # return render(request, 'login.html', {'login_form': form})

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