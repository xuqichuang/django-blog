"""djangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from rest_framework.schemas import get_schema_view
from django.contrib import admin

import xadmin
from django.views.generic.base import TemplateView
from users.views import login,logOut,register
from users.api import user_list,ajax_dict,ajax_list
from aboutMe.views import AboutMeList
from blog.views import BlogList,GetBlog,GetTagList,GetArticleTagList,ClickBlogList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"),name='index'),
    url(r'^api/login', login,name='login'),
    url(r'^api/logOut', logOut,name='logOut'),
    url(r'^api/register', register,name='register'),
    url(r'^docs/', get_schema_view(),name='docs'),
    url(r'^api/user_list',user_list,name='user_list'),
    url(r'^api/ajax_dict',ajax_dict,name='ajax_dict'),
    url(r'^api/ajax_list',ajax_list,name='ajax_list'),
    url(r'^api/AboutMeList', AboutMeList, name='aboutMeList'),
    url(r'^api/blogList', BlogList, name='blogList'),
    url(r'^api/clickBlogList', ClickBlogList, name='clickBlogList'),
    url(r'^api/getBlog', GetBlog, name='getBlog'),
    url(r'^api/getTagList', GetTagList, name='getArticleTagList'),
    url(r'^api/getArticleTagList', GetArticleTagList, name='getArticleTagList'),
]

