from django.conf.urls import url, include
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import settings

from . import views

urlpatterns = [
  #url(r'^(?P<advertisement_id>[0-9]+)/$', views.view),
  #url(r'^$', views.AdvListView.as_view(), name='index'),
  # url(r'^(?P<pk>[0-9]+)/$', views.AdvDetailView.as_view(), name='view'),

  # url(r'^(?P<advertisement_id>[0-9]+)/$', views.view, name='view'),
  # url(r'^page/(?P<page_number>[0-9]+)/$', views.list, name='list'),
  # url(r'^new/$', views.new, name='new'),
  # url(r'^(?P<advertisement_id>[0-9]+)/edit/$', views.edit, name='edit'),

  url(r'^bicycle/$'                                 ,views.bicycles       ,name='bicycles'),
  url(r'^bicycle/page/(?P<page_number>[0-9]+)/$'    ,views.bicycles       ,name='bicycles'),
  url(r'^bicycle/new/$'                             ,views.new_bicycle    ,name='new_bicycle',),
  url(r'^bicycle/(?P<bicycle_id>[0-9]+)/$'          ,views.view_bicycle   ,name='view_bicycle'),
  url(r'^bicycle/(?P<bicycle_id>[0-9]+)/edit/$'     ,views.edit_bicycle   ,name='edit_bicycle'),
  url(r'^bicycle/(?P<bicycle_id>[0-9]+)/delete/$'   ,views.delete_bicycle ,name='delete_bicycle'),

  url(r'^ski/$'                                     ,views.skis         ,name='skis'),
  url(r'^ski/page/(?P<page_number>[0-9]+)/$'        ,views.skis         ,name='skis'),
  url(r'^ski/new/$'                                 ,views.new_ski      ,name='new_ski'),
  url(r'^ski/(?P<ski_id>[0-9]+)/$'                  ,views.view_ski     ,name='view_ski'),
  url(r'^ski/(?P<ski_id>[0-9]+)/edit/$'             ,views.edit_ski     ,name='edit_ski'),

  url(r'^$'                                         ,views.categories   ,name='categories'),
]

# if settings.DEBUG:
#     urlpatterns += staticfiles_urlpatterns() + static(
#     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
