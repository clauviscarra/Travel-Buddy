# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages


def home(request):

    return render(request, 'login_app/home.html')

def index(request):

    return render(request,'login_app/login.html')

def login(request):
    result = User.objects.login(request.POST)
    request.session['user_name'] = request.POST['username']

    if result == True:
        return redirect('travels/')
    else:
        for i in result[1]:
            messages.info(request,i)
        return redirect ('/log-in')

def register(request):
    return render (request,'login_app/register.html')

def register_process(request):
    result2 = User.objects.register(request.POST)
    request.session['user_name'] = request.POST['username']

    if result2[0]:
        return redirect ('/travels')

    else:
        for i in result2[1]:
            messages.info(request,i)
        return redirect ('/register')

def logout(request):
    print request.session['user_name']
    request.session.clear()
    return redirect ('/')
