# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from .models import EmailVerifyRecord,Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GloableSettings(object):
    site_title = '一叶障目的后台管理系统'
    site_footer = '版权所有：一叶障目'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display= ['code','email','send_type','send_time']
    search_fields= ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']


class BannerAdmin(object):
    list_display = ['title', 'url', 'index', 'add_time']
    search_fields = ['title', 'url', 'index']
    list_filter = ['title', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GloableSettings)