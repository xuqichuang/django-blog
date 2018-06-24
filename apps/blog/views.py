# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.utils import json
from rest_framework import serializers

from .models import Blog,ArticleTag,BlogType

# Create your views here.


class BlogSerializers(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'
        depth = 2


class ArticleTagSerializers(serializers.ModelSerializer):

    class Meta:
        model = ArticleTag
        fields = ('id','tag')


def BlogList(request):
    if request.method == 'POST':
        if request.body.decode() != '':
            params = json.loads(request.body.decode())
            blogType_id = params['blogType_id']
            dataList = Blog.objects.filter(blogType_id=blogType_id).order_by('-add_time')
        else:
            dataList = Blog.objects.all().order_by('-add_time')[0:6]

        serializer = BlogSerializers(instance=dataList,many=True)
        return HttpResponse(json.dumps(serializer.data))


def ClickBlogList(request):
    if request.method == 'POST':

        dataList = Blog.objects.all().order_by('-click_num')[0:6]

        serializer = BlogSerializers(instance=dataList,many=True)
        return HttpResponse(json.dumps(serializer.data))


def GetBlog(request):
    if request.method == 'POST':
        params = json.loads(request.body.decode())
        id = params['id']
        data = Blog.objects.filter(id=id)
        click_num = list(data.values_list('click_num', flat=True))
        click_num[0] += 1
        print(click_num)
        data.update(click_num=click_num[0])
        serializer = BlogSerializers(instance=data, many=True)
        return HttpResponse(json.dumps(serializer.data))


def GetTagList(request):
    if request.method == 'POST':
        if request.body.decode() != '':
            params = json.loads(request.body.decode())
            id = params['id']
            dataList = ArticleTag.objects.filter(id=id)
        else:
            dataList = ArticleTag.objects.all()

        serializer = ArticleTagSerializers(instance=dataList, many=True)
        return HttpResponse(json.dumps(serializer.data))


def GetArticleTagList(request):
    if request.method == 'POST':
        params = json.loads(request.body.decode())
        print(params)
        article_tag_id = params['article_tag_id']
        data = Blog.objects.filter(article_tag_id=article_tag_id).order_by('-add_time')

        serializer = BlogSerializers(instance=data, many=True)
        return HttpResponse(json.dumps(serializer.data))

