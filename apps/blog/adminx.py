# -*- coding: utf-8 -*-
__author__ = 'xuqichuang'
__date__ = '2018/5/31 0031 20:33'

import xadmin

from .models import ArticleTag,BlogType,Blog


class ArticleTagAdmin(object):
    list_display = ['tag','add_time']
    search_fields = ['tag']
    list_filter = ['tag','add_time']


class BlogTypeAdmin(object):
    list_display = ['type','add_time']
    search_fields = ['type']
    list_filter = ['type','add_time']


class BlogAdmin(object):
    list_display = ['title','author','click_num','blogType','article_tag']
    search_fields = ['title','author','click_num','blogType','article_tag']
    list_filter = ['title','author','click_num','blogType','article_tag']




xadmin.site.register(ArticleTag,ArticleTagAdmin)
xadmin.site.register(BlogType,BlogTypeAdmin)
xadmin.site.register(Blog,BlogAdmin)