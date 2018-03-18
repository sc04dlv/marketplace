from django.conf.urls import url

from . import views

urlpatterns = [
  #url(r'^(?P<advertisement_id>[0-9]+)/$', views.view),
  #url(r'^$', views.AdvListView.as_view(), name='index'),
  # url(r'^(?P<pk>[0-9]+)/$', views.AdvDetailView.as_view(), name='view'),

  url(r'^(?P<advertisement_id>[0-9]+)/$', views.view, name='view'),
  url(r'^page/(?P<page_number>[0-9]+)/$', views.list, name='list'),
  url(r'^new/$', views.new, name='new'),
  url(r'^(?P<advertisement_id>[0-9]+)/edit/$', views.edit, name='edit'),

  url(r'^bicycle/(?P<advertisement_id>[0-9]+)/$', views.view_bicycle, name='view_bicycle'),
  url(r'^bicycle/(?P<advertisement_id>[0-9]+)/edit/$', views.edit_bicycle, name='edit_bicycle'),

  url(r'^$',views.list, name='list')
]
