from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:product_list'))
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def registration(request):
    return render(request, 'users/registration.html')

def profile(request):
    return render(request, 'users/profile.html')

def logout(request):
    ...