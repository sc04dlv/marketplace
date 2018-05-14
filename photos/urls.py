from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^advertisement/(?P<adv_id>[0-9]+)/delete/$', views.clear_adv_photo, name='clear_adv_photo'),
    # url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),

    url(r'^advertisement/(?P<adv_id>[0-9]+)/edit/$', views.AdvertisementPhotoEditView.as_view(), name='advertisement_photo_edit'),


    # url(r'^progress-bar-upload/$', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    # url(r'^drag-and-drop-upload/$', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
]
