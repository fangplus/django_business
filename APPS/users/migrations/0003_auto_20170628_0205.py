# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-28 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170622_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='user_image/%Y/%m/'),
        ),
    ]