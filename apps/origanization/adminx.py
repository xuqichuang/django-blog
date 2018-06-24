# -*- coding: utf-8 -*-
__author__ = 'xuqichuang'
__date__ = '2018/5/31 0031 20:33'

import xadmin

from .models import CityDict,CourseOrg,Teacher


class CityDictAdmin(object):
    list_display = ['name','desc','add_time']
    search_fields = ['name','desc']
    list_filter = ['name','desc','add_time']

class CourseOrgAdmin(object):
    list_display = ['city', 'name', 'desc','click_num','fav_num','add_time']
    search_fields = ['city', 'name', 'desc','click_num','fav_num']
    list_filter = ['city', 'name', 'desc','click_num','fav_num','add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years','work_company','work_position','points','click_num','fav_num','add_time']
    search_fields = ['org', 'name', 'work_years','work_company','work_position','points','click_num','fav_num']
    list_filter = ['org', 'name', 'work_years','work_company','work_position','points','click_num','fav_num','add_time']


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)