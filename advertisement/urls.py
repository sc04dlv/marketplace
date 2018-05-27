#coding: utf-8

from django.conf.urls import url, include
from . import views

urlpatterns = [
  url(r'^user/(?P<user_id>[0-9]+)/$'
                                                    ,views.user_advertisements ,name='user_advertisements'),
  url(r'^user/(?P<user_id>[0-9]+)/page/(?P<page_number>[0-9]+)/$'
                                                    ,views.user_advertisements ,name='user_advertisements'),

  # при добавлении нового типа добавить тип с url в таблицу advertisement_type
  url(r'^bicycle/$'                                 ,views.bicycles       ,name='bicycles'),
  url(r'^bicycle/page/(?P<page_number>[0-9]+)/$'    ,views.bicycles       ,name='bicycles'),
  url(r'^bicycle/new/$'                             ,views.new_bicycle    ,name='new_bicycle',),
  url(r'^bicycle/(?P<adv_id>[0-9]+)/$'          ,views.view_bicycle   ,name='view_bicycle'),
  url(r'^bicycle/(?P<adv_id>[0-9]+)/edit/$'     ,views.edit_bicycle   ,name='edit_bicycle'),
  url(r'^bicycle/(?P<adv_id>[0-9]+)/delete/$'   ,views.delete_bicycle ,name='delete_bicycle'),

  url(r'^ski/$'                                     ,views.skis           ,name='skis'),
  url(r'^ski/page/(?P<page_number>[0-9]+)/$'        ,views.skis           ,name='skis'),
  url(r'^ski/new/$'                                 ,views.new_ski        ,name='new_ski'),
  url(r'^ski/(?P<adv_id>[0-9]+)/$'                  ,views.view_ski       ,name='view_ski'),
  url(r'^ski/(?P<adv_id>[0-9]+)/edit/$'             ,views.edit_ski       ,name='edit_ski'),

  url(r'^$'                                         ,views.categories     ,name='categories'),
]
