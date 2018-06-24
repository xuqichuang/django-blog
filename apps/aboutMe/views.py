# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.utils import json
from rest_framework import serializers

from .models import AboutMe

# Create your views here.


class AboutMeSerializers(serializers.ModelSerializer):

    class Meta:
        model = AboutMe
        fields = ('add_time','description')


def AboutMeList(request):
    if request.method == 'POST':
        dataList = AboutMe.objects.all().order_by('-add_time')
        serializer = AboutMeSerializers(dataList,many=True)
        return HttpResponse(json.dumps(serializer.data))
