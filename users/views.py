# from typing_extensions import ParamSpec
from django.contrib.auth.models import User
from django.http.request import HttpRequest 
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


from .forms import LoginForm, SignupForm

# Index page
def index(request):
    return render(request, 'users/index.html')

# Account page
def account(request):
    return render(request, 'users/account.html')

# sigup page
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            student = User.objects.create_user(username=username, email=email, password=password)

            # save the new student to the db
            student.save(update_fields=['username', 'email', 'password'])

            # Redirect users to a login page
            return HttpResponseRedirect('/accounts/login/')

    else:
        # Send an empty signup form
        form = SignupForm()
        return render(request, 'users/signup.html', {'form': form})

# login page
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            student = authenticate(request, username=username, password=password)

            if student is not None:
                
                print({'username': student.username, 'is_authenticated': student.is_authenticated})

                login(request, student)

                print({'username': student.username, 'is_authenticated': student.is_authenticated})

                return HttpResponseRedirect('/accounts/', {'student': student})
            else:
                return HttpResponseRedirect('/login-error/')
    else:
        # send an empty login form
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})

# logout page
def logout_view(request):
    logout(request)
    
    return HttpResponseRedirect('/')

def clear_db(request):
    User.objects.all().delete()

    return HttpResponseRedirect('/accounts/signup/')

def view_db(request):
    users = User.objects.all()

    return render(request, 'users/users.html', {'users': users})

@login_required(login_url='/accounts/login/')
def restricted(request):
    return render(request, 'users/restricted.html')