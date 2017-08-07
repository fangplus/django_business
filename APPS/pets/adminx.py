# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
_date_ = '2017/6/22 14:53'

import xadmin

from .models import PetInformation


class PetInformation_adminx(object):

    list_display = ['pet_org', 'name', 'des', 'detail', 'price', 'buy_people_num', 'age', 'pet_type', 'pet_image', 'click_nums', 'add_time']

    search_field = ['pet_org', 'name', 'des', 'detail', 'price', 'buy_people_num', 'age', 'pet_type', 'pet_image', 'click_nums']

    list_filter = ['pet_org', 'name', 'des', 'detail', 'price', 'buy_people_num', 'age', 'pet_type', 'pet_image', 'click_nums', 'add_time']

xadmin.site.register(PetInformation, PetInformation_adminx)

