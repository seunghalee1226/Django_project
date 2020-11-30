"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from notice import views

app_name = 'notice'

urlpatterns = [

    # /notice/
    path('', views.PostLV.as_view(), name='index'),

    # /notice/notice/
    path('notice/', views.PostLV.as_view(), name='notice_list'),

    # /notice/notice/django-example.
    re_path(r'^notice/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='notice_detail'),

    # /notice/archive
    path('archive/', views.PostAV.as_view(), name='notice_archive'),

    # /notice/archive/2019
    path('archive/<int:year>', views.PostYAV.as_view(), name='notice_year_archive'),

    # /notice/archive/2019/nov
    path('archive/<int:year>/<int:month>/', views.PostMAV.as_view(), name='notice_month_archive'),

    # /notice/archive/2019/nov/10
    path('archive/<int:year>/<int:month>/<int:day>/', views.PostDAV.as_view(), name='notice_day_archive'),

    # /notice/archive/today
    path('archive/today/', views.PostTAV.as_view(), name='notice_today_archive'),
]
