# _*_ coding:utf-8 _*_
"""Djangobusiness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin
from users.views import LoginView, ResiterView, ActiceUserView, ForgetPwsView, ResetView, ModifyPwdView
from organization.views import org_list
from Djangobusiness.settings import MEDIA_ROOT


urlpatterns = (
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^register/$', ResiterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiceUserView.as_view(), name="active"),
    url(r'^forget/$', ForgetPwsView.as_view(), name="forgetpwd"),

    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),

    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 配置上传图片的配置

    # 宠物店铺url配置
    url(r'^org/', include('organization.org_url', namespace="org")),
    url(r'^org/', include('organization.org_url', namespace="org_teacher")),

    # 宠物url配置
    url(r'^pet/', include('pets.pet_url', namespace="pet")),
    url(r'^course/', include('pets.pet_url', namespace="pet_course")),

    #用户url配置
    url(r'^users/', include('users.user_url', namespace="users")),





)
