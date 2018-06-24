# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from users.models import UserProfile

# Create your models here.

class ArticleTag(models.Model):
    tag = models.CharField(max_length=50,verbose_name=u'文章标签')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'文章标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tag


class BlogType(models.Model):
    type = models.CharField(max_length=50, verbose_name=u'博客类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'博客类型'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.type



class Blog(models.Model):
    blogType = models.ForeignKey(BlogType,verbose_name=u'博客类型')
    article_tag = models.ForeignKey(ArticleTag,verbose_name=u'文章标签', on_delete=models.CASCADE)
    author = models.CharField(max_length=50,verbose_name=u'作者')
    title = models.CharField(max_length=50,verbose_name=u'文章标题')
    click_num = models.IntegerField(default=0,verbose_name=u'点击人数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    content = models.TextField(verbose_name=u'文章内容')
    image = models.ImageField(upload_to='article/%Y/%m',verbose_name=u'文章图片',max_length=100,null=True,blank=True)

    class Meta:
        verbose_name = u'博客'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
