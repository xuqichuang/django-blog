# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/%Y/%m', verbose_name='\u5c01\u9762\u56fe'),
        ),
    ]