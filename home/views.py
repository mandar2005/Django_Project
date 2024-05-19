# home/views.py
from multiprocessing import context
from django.shortcuts import render , HttpResponse , get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm



def index(request):
    return render(request, 'home/index.html')

def private(request):
    return render(request, 'home/private.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'home/private.html')
        else:
            # Handle invalid login
            return  HttpResponse("Invalid Credential")

    return render(request, 'home/login.html')



def logout_view(request):
    logout(request)
    return render(request, 'home/login.html')

# views.py
 

def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'home/index.html')  # Redirect to the home page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

