# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-26 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20170626_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet_organization',
            old_name='buy_nums',
            new_name='click_nums',
        ),
    ]
