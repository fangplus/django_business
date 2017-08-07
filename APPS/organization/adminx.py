# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
_date_ = '2017/6/22 15:02'

import xadmin

from .models import City
from .models import pet_organization
from .models import pet_boss


class City_xadmin(object):
    list_display = ['name', 'des', 'add_time']
    search_field = ['name', 'des']
    list_filter = ['name', 'des', 'add_time']


class pet_organization_xadmin(object):
    list_display = ['name', 'des', 'click_nums', 'favorite_nums', 'org_image', 'address', 'city', 'add_time']
    search_field = ['name', 'des', 'click_nums', 'favorite_nums', 'org_image', 'address', 'city']
    list_filter = ['name', 'des', 'click_nums', 'favorite_nums', 'org_image', 'address', 'city', 'add_time']


class pet_boss_xadmin(object):
    list_display = ['work_org', 'name', 'work_year', 'click_nums', 'favorite_nums', 'add_time']
    search_field = ['work_org', 'name', 'work_year', 'click_nums', 'favorite_nums']
    list_filter = ['work_org', 'name', 'work_year', 'click_nums', 'favorite_nums', 'add_time']

xadmin.site.register(City, City_xadmin)
xadmin.site.register(pet_organization, pet_organization_xadmin)
xadmin.site.register(pet_boss, pet_boss_xadmin)