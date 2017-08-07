# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime


from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="宠物")
    birday = models.DateTimeField(verbose_name=u"生日", blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(("male", u"男"), ("female", u"女")), default="female")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, blank=True, null=True)
    image = models.ImageField(upload_to="user_image/%Y/%m/", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):   #chongzai print UserProfile,buenng zhengchang dayin
        return self.username


class EmailVerifyRecord(models.Model):
     code = models.CharField(max_length=25, verbose_name=u"验证码")
     email = models.EmailField(max_length=50, verbose_name=u"邮箱")
     send_type = models.CharField(max_length=10, choices=(("register", u"注册"), ("forget", u"忘记密码")), verbose_name=u"验证类型")
     send_time = models.DateTimeField(default=datetime.now, verbose_name=u"验证时间")

     class Meta:
         verbose_name = u"用户邮箱验证"
         verbose_name_plural = verbose_name

     # 如同上面，通过重载unicode的方法，在后台管理界面显示相对应的字段，这里选择显示了验证码和邮箱
     def __unicode__(self):
        return '{0}:{1}'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(max_length=100, verbose_name=u"图片", upload_to="banner/%Y/%m/%d")
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"滑动图片"
        verbose_name_plural = verbose_name
