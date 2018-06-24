# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.


class AboutMe(models.Model):
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    description = models.TextField(verbose_name=u'当日事件')


    class Meta:
        verbose_name = '关于我'
        verbose_name_plural = verbose_name
