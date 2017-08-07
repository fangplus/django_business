# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"城市")
    des = models.CharField(max_length=200, verbose_name=u"城市描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class pet_organization(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"店名")
    des = models.TextField(verbose_name=u"店铺描述")
    catgory = models.CharField(max_length=20, choices=(("wgsc", "宠物公司"), ("zz", "组织"), ("gr", "个人")), verbose_name="店铺类别", default="zz")
    org_image = models.ImageField(upload_to="org_logo/%Y/%m", verbose_name=u"宠物店铺logo", max_length=100)
    address = models.CharField(max_length=100, verbose_name=u"实体店地址")
    city = models.ForeignKey(City, verbose_name=u"店铺城市")
    click_nums = models.IntegerField(default=0, verbose_name=u"购买数")
    favorite_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    pet_nums = models.IntegerField(default=0, verbose_name=u"宠物数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"店铺"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class pet_boss(models.Model):
    work_org = models.ForeignKey(pet_organization, verbose_name=u"boss店铺")
    name = models.CharField(max_length=50, verbose_name=u"老板名字")
    work_year = models.IntegerField(default=0, verbose_name=u"开店年龄")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    favorite_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    boss_image = models.ImageField(upload_to="boss_image/%Y/%m", verbose_name=u"店铺老板头像", max_length=100, null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"店铺boss信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
