# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from django.views.generic import View

def logout_user(request):
    
    logout(request)
    return redirect('login')
    