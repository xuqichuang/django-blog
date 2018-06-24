# -*- coding: utf-8 -*-
__author__ = 'xuqichuang'
__date__ = '2018/5/31 0031 20:33'

import xadmin

from .models import AboutMe


class AboutMeAdmin(object):
    list_display = ['description','add_time']
    search_fields = ['description']
    list_filter = ['description','add_time']



xadmin.site.register(AboutMe,AboutMeAdmin)