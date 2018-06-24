# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.utils import json

from rest_framework.views import APIView
from dss.Serializer import serializer
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import redirect

from django.forms import ModelForm
from users.models import UserProfile

import time
# Create your views here.

def login(request):
    nowTime = time.strftime(format("%Y-%m-%d %H:%M:%S"))
    if request.method == 'POST':
        user_obj = json.loads(request.body.decode())
        print(user_obj)
        username = user_obj['username']
        password = user_obj['password']
        user = authenticate(username = username,password = password )
        arr = [111,222,333,"都是测试数据"]
        if user is not None and user.is_active:
            auth.login(request,user)
            return HttpResponse(json.dumps({'token':arr,'message':'登录成功'}))
        else:
            return HttpResponse(json.dumps({'arr':arr,'message':'用户名或密码错误'}))


def logOut(request):
    arr = [111, 222, 333, "都是测试数据"]
    auth.logout(request)
    return HttpResponse(json.dumps({'arr':arr,'message':'退出登录'}))


#注册表单
class RegisterForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']



def register(request):
    if request.method == 'POST':
        user_obj = json.loads(request.body.decode())
        username = user_obj['username']
        pass_word = user_obj['password']
        user_model = list(UserProfile.objects.all().values_list('username',flat=True))
        if username not in user_model:
            users = UserProfile.objects.create_user(username=username, password=pass_word)
            user = authenticate(username=username, password=pass_word)
            UserProfile.save(users)
            auth.login(request, user)
            return HttpResponse(json.dumps({'arr':user_model,'message':'注册成功'}))
        else:
            return HttpResponse(json.dumps({'arr':user_model,'message':'用户名已存在'}))


