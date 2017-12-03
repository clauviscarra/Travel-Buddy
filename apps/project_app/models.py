# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
from datetime import datetime
import re
date_regex = re.compile(r'^(\d+-\d+-\d+)+$')


class UserManager(models.Manager):
    def add_plan(self, plan_data, session):
        flag = True
        errors = []


        if len(plan_data['destination']) < 1:
            flag = False
            errors.append('Please enter a destination.')
        if len(plan_data['description']) < 1:
            flag = False
            errors.append('Please enter a description.')

        if not date_regex.match(plan_data['date_from']) or not date_regex.match(plan_data['date_to']):
            errors.append('Please enter a date with the correct format.')
            return (False,errors)


        if not plan_data['date_from'] or not plan_data['date_to']:
            return (False, errors)
            errors.append('Please fill your date file propperly.')

        startdate = datetime.strptime(plan_data['date_from'],'%Y-%m-%d')
        endate = datetime.strptime(plan_data['date_to'],'%Y-%m-%d')

        if endate < startdate:
            flag = False
            errors.append('You cannot travel in time, silly.')
        elif startdate < datetime.now():
            flag = False
            errors.append('Trip must be in the future.')

        if flag:
            new_plan = Travel.objects.create(destination=plan_data['destination'], description=plan_data['description'], date_from=plan_data['date_from'],date_to=plan_data['date_to'], created_by=session)
            return (True, new_plan)
        else:
            return (False, errors)

class Travel(models.Model):
    destination = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    date_from= models.DateField()
    date_to= models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_travel = models.ForeignKey(User,default=True,related_name='travel_user')
    created_by = models.CharField(max_length=255, default = True)

    objects = UserManager()
    def __str__(self):
        return self.name

class User_Travel(models.Model):
    travel = models.ForeignKey(Travel, related_name='travel_destination')
    user = models.ForeignKey(User, related_name='user_name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
