# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class UserManager(models.Manager):
    def login(self, login_data):
        flag = True
        errors = []
        if  len(login_data['username']) < 3:
            flag = False
            errors.append('Please enter e-mail')
        if  len(login_data['password']) < 8:
            flag = False
            errors.append('Please enter password')
        if not User.objects.filter(email = login_data['username']):
            flag = False
            errors.append('You are not in our data base, please register.')
        if not User.objects.filter(password = login_data['password']):
            flag = False
            errors.append('Your password is incorrect.')

        if flag:
            return True
        else:
            return (False, errors)
    def register(self, register_data):
        flag = True
        errors =[]

        if len(register_data['first_name']) < 3:
            flag = False
            errors.append('Please enter name.')

        if  len(register_data['username']) < 1:
            flag = False
            errors.append('Please enter user name')
        if User.objects.filter(email=register_data['username']):
            flag = False
            errors.append('User name already taken, please choose a different one.')

        if  len(register_data['password']) < 1:
            flag = False
            errors.append('Please enter password.')
        elif (register_data['password']) != (register_data['confirm']):
            errors.append('Password does not match.')
            flag = False
        if flag:
            new_user = User.objects.create(first_name=register_data['first_name'], email=register_data['username'], password=register_data['password'])
            return (True, new_user)
        else:
            return (False, errors)

class User(models.Model):
    first_name=models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

# Create your models here.
