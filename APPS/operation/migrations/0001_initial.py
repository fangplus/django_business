# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-22 03:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pet_comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200, verbose_name='\u5ba0\u7269\u8bc4\u8bba')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u8bc4\u8bba',
                'verbose_name_plural': '\u7528\u6237\u8bc4\u8bba',
            },
        ),
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u59d3\u540d')),
                ('mobile', models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7\u7801')),
                ('course_name', models.CharField(max_length=50, verbose_name='\u8bfe\u7a0b\u540d\u79f0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u54a8\u8be2',
                'verbose_name_plural': '\u7528\u6237\u54a8\u8be2',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='\u6570\u636eID')),
                ('fav_type', models.IntegerField(choices=[(1, '\u5ba0\u7269'), (2, '\u5ba0\u7269\u5e97'), (3, '\u5ba0\u7269boss')], default=1)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6536\u85cf',
                'verbose_name_plural': '\u7528\u6237\u6536\u85cf',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='\u63a5\u6536\u7528\u6237')),
                ('message', models.CharField(max_length=500, verbose_name='\u63a5\u6536\u4fe1\u606f')),
                ('has_read', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u8bfb')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6d88\u606f',
                'verbose_name_plural': '\u7528\u6237\u6d88\u606f',
            },
        ),
        migrations.CreateModel(
            name='UserPet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.PetInformation', verbose_name='\u5ba0\u7269')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u5ba0\u7269',
                'verbose_name_plural': '\u7528\u6237\u5ba0\u7269',
            },
        ),
    ]
