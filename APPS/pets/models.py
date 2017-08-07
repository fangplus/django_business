# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from organization.models import pet_organization

# Create your models here.


class PetInformation(models.Model):
    pet_org = models.ForeignKey(pet_organization, verbose_name=u"宠物店铺", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"宠物名称")
    des = models.CharField(max_length=300, verbose_name=u"宠物描述")
    detail = models.TextField(verbose_name=u"宠物详情")
    price = models.IntegerField(verbose_name=u"宠物价格", default=100)
    buy_people_num = models.IntegerField(verbose_name=u"购买人数", default=100)
    age = models.FloatField(verbose_name=u"宠物年龄", default=1.5)
    pet_type = models.CharField(max_length=50, verbose_name=U"宠物类别")
    pet_image = models.ImageField(upload_to="pets/%Y/%m", verbose_name=u"宠物封面图片", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"宠物信息"
        verbose_name_plural = verbose_name
