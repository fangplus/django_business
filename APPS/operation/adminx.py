# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
_date_ = '2017/6/22 15:02'

import xadmin

from .models import UserAsk
from .models import pet_comments
from .models import UserFavorite
from .models import UserMessage
from .models import UserPet

class UserAsk_xadmin(object):
    list_display = ['name', 'mobile', 'pet_name', 'add_time']
    search_field = ['name', 'mobile', 'pet_name']
    list_filter =['name', 'mobile', 'pet_name', 'add_time']


class pet_comments_xadmin(object):
    list_display = ['user', 'pet', 'comments', 'add_time']
    search_field = ['user', 'pet', 'comments']
    list_filter = ['user', 'pet', 'comments', 'add_time']


class UserFavorite_xadmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_field = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessage_xadmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_field = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserPet_xadmin(object):
    list_display = ['user', 'pet', 'add_time']
    search_field = ['user', 'pet']
    list_filter = ['user', 'pet', 'add_time']


xadmin.site.register(UserAsk, UserAsk_xadmin)
xadmin.site.register(pet_comments, pet_comments_xadmin)
xadmin.site.register(UserFavorite, UserFavorite_xadmin)
xadmin.site.register(UserMessage, UserMessage_xadmin)
xadmin.site.register(UserPet, UserPet_xadmin)
