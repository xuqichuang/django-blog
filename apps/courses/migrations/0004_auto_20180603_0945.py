# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-03 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180531_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseresource',
            name='download',
            field=models.FileField(upload_to='courses/resource/%Y/%M', verbose_name='\u4e0b\u8f7d\u5730\u5740'),
        ),
    ]
