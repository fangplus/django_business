# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfile
from pets.models import PetInformation


# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"姓名")
    mobile = models.CharField(max_length=11, verbose_name=u"手机号码")
    pet_name = models.CharField(max_length=50, verbose_name=u"宠物名称", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name


class pet_comments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    pet = models.ForeignKey(PetInformation, verbose_name=u"宠物")
    comments = models.CharField(max_length=200, verbose_name=u"宠物评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据ID")
    fav_type = models.IntegerField(choices=((1, "宠物"),(2, "宠物店"),(3, "宠物boss")), default=1)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    message = models.CharField(max_length=500, verbose_name=u"接收信息")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserPet(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    pet = models.ForeignKey(PetInformation, verbose_name=u"宠物")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户宠物"
        verbose_name_plural = verbose_name
