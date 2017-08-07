# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-26 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20170626_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet_organization',
            name='click_nums',
        ),
        migrations.AddField(
            model_name='pet_organization',
            name='buy_nums',
            field=models.IntegerField(default=0, verbose_name='\u8d2d\u4e70\u6570'),
        ),
        migrations.AddField(
            model_name='pet_organization',
            name='pet_nums',
            field=models.IntegerField(default=0, verbose_name='\u5ba0\u7269\u6570'),
        ),
    ]