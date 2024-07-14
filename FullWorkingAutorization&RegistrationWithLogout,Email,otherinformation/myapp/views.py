from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import main
from .forms import RegisterUserForm
from .utils import *


main_id_number = 1


@login_required(login_url='/login/')
def main(request):
    if isRequestPost(request):
        testmain = main.objects.get(id=main_id_number)
        new_message = createMessage(request, testmain)
        serialized_message = serializeJson(request, new_message)
        return JsonResponse(serialized_message, safe=False)
    main_messages = filtermainMessages(main_id_number)
    return render(
        request,
        'main.html',
        {'main_messages': main_messages}
    )


def login_user(request):
    redirect_extract = request.GET.get('next')
    if isRequestPost(request):
        user = authenticate(
            username = request.POST.get('username'),
            password = request.POST.get('password')
        )
        if isUserExist(user):
            login(request, user)
            if redirect_extract=='next':
                return HttpResponseRedirect(
                    request.POST.get('redirect_extract')
                )
            else:
                return redirect('main')
        else:
            return render(
                request,
                'login.html',
                {'wrongPassword': True},
                {'redirect':redirect_extract}
            )
    return render(request, 'login.html', {'redirect': redirect_extract})


def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Logged Out."))
    return redirect('login_user')


def registry_user(request):
    if isRequestPost(request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form, })