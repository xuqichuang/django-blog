# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-03 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180531_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y/%m'),
        ),
    ]
