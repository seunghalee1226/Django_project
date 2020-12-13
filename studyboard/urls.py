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
from studyboard import views

app_name = 'studyboard'

urlpatterns = [

    # /studyboard/
    path('', views.PostLV.as_view(), name='index'),

    # /studyboard/post/
    path('studyboard/', views.PostLV.as_view(), name='studyboard_list'),

    # /studyboard/post/django-example.
    re_path(r'^studyboard/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='studyboard_detail'),

    # /studyboard/archive
    path('archive/', views.PostAV.as_view(), name='studyboard_archive'),

    # /studyboard/archive/2019
    path('archive/<int:year>', views.PostYAV.as_view(), name='studyboard_year_archive'),

    # /studyboard/archive/2019/nov
    path('archive/<int:year>/<int:month>/', views.PostMAV.as_view(), name='studyboard_month_archive'),

    # /studyboard/archive/2019/nov/10
    path('archive/<int:year>/<int:month>/<int:day>/', views.PostDAV.as_view(), name='studyboard_day_archive'),

    # /studyboard/archive/today
    path('archive/today/', views.PostTAV.as_view(), name='studyboard_today_archive'),

    # /studyboard/tag/
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),

    # /studyboard/tag/tagname/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),

    # /studylog/search
    path('search/', views.SearchFormView.as_view(), name='search'),
    
]
