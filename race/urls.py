#coding: utf-8

from django.conf.urls import url, include
from . import views

urlpatterns = [
  url(r'^(?P<race_code>[\w-]+)/milestones/$'                                ,views.milestones           ,name='milestones'),
  url(r'^(?P<race_code>[\w-]+)/milestones/check/(?P<milestone_id>[0-9]+)$'  ,views.milestone_check      ,name='milestone_check'),
  url(r'^(?P<race_code>[\w-]+)/milestones/remove/(?P<protocol_id>[0-9]+)$'  ,views.milestone_remove     ,name='milestone_remove'),

  url(r'^(?P<race_code>[\w-]+)/protocol/$'                                  ,views.protocol_all         ,name='protocol_all'),
  url(r'^(?P<race_code>[\w-]+)/protocol/(?P<user_name>[\w-]+)$'             ,views.protocol_user        ,name='protocol_user'),

  url(r'^(?P<race_code>[\w-]+)$'                                            ,views.race_home            ,name='race_home'),
  url(r'^(?P<race_code>[\w-]+)/registration$'                               ,views.registration         ,name='registration'),
  url(r'^(?P<race_code>[\w-]+)/registration/remove$'                        ,views.registration_remove  ,name='registration_remove'),
  url(r'^$'                                                                 ,views.race_select          ,name='race_select'),
]
