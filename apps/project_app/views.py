# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Travel, User_Travel, User
from django.shortcuts import render, redirect
from django.contrib import messages
from sets import Set


def travels(request):
    a = set(Travel.objects.all())
    b= set(Travel.objects.filter(travel_destination__user__email=request.session['user_name']))
    excluded_travels = (a.difference(b))
    context = {
    'user_plans' : User_Travel.objects.filter(user__email = request.session['user_name']),
    'all_other_user_plans': excluded_travels,
    'all_users':User.objects.all()
    }

    return render (request,'project_app/index.html', context)
def add_plan(request):
    return render (request,'project_app/add_plan.html')

def process_travel(request):
    session = request.session['user_name']
    process_result = Travel.objects.add_plan(request.POST, session)


    if process_result[0]:


        t1 = Travel.objects.filter(destination = request.POST['destination'])
        u1 = User.objects.filter(email = request.session['user_name'])

        travel_join = User_Travel.objects.create(user=u1[0], travel=t1[0])
        return redirect ('/travels')

    else:
        for i in process_result[1]:
            messages.info(request,i)
        return redirect ('/travels/add')

def destination(request, id_):
    context ={
    'users_filter':User_Travel.objects.filter(travel_id=id_).exclude(user__email=request.session['user_name']),
    'other_users':Travel.objects.filter(id=id_),
    }
    return render(request,'project_app/destination.html', context)
def join(request, team_id):
    t1 = Travel.objects.filter(id = team_id)
    u1 = User.objects.filter(email = request.session['user_name'])

    trip_join = User_Travel.objects.create(user=u1[0], travel=t1[0])

    return redirect ('/travels')

def remove(request, team_id):
    User_Travel.objects.filter(travel__id=team_id).filter(user__email=request.session['user_name']).delete()
    
    return redirect('/travels')

# Create your views here.
