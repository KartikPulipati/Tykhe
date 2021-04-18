from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'UserAuth/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('listTodo')
            except IntegrityError:
                return render(request, 'UserAuth/signupuser.html', {'form': UserCreationForm(),
                                                                    'UseError': 'Username Not Avaible, Please Enter A Different Username!'})
        else:
            return render(request, 'UserAuth/signupuser.html',
                          {'form': UserCreationForm(), 'PasError': 'Passwords Do Not Match!'})

@login_required(login_url='loginuser')
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'UserAuth/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'UserAuth/loginuser.html', {'form': AuthenticationForm(), 'error': 'This User Does Not Exist, Please Try Again'})
        else:
            login(request, user)
            return redirect('listTodo')
