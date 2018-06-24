# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse
from rest_framework.utils import json

from .models import UserProfile


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        # fields = '__all__'  全部展示
        fields = ('username','email','address','image')


def user_list(request):
    if(request.method == "POST"):
        user_list = UserProfile.objects.all()
        serializer = UserSerializers(user_list,many=True)
        return HttpResponse(json.dumps(serializer.data))


def ajax_list(request):
    data = request.POST
    print(request)
    print(data.get('nick_name'))
    # UserProfile.objects.create(nick_name=u'xuqichuang',address=u'吉林')
    a = range(100)
    return HttpResponse(a,safe=False)

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return HttpResponse(name_dict)


