#coding: utf-8
import time

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.template.context_processors import csrf

from .forms import PhotoForm
from .models import Photo

from advertisement.models import Advertisement

import time

class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        for photo in photos_list:
            print(photo.file_small.url)
        return render(self.request, 'photos/base.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            # print(photo.file_small.url)
            data = {'is_valid': True, 'url_small': photo.file_small.url, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)



####### ADVERTISEMENT_PHOTO #######
class AdvertisementPhotoEditView(View):
    def get(self, request, adv_id):
        args = {}
        args['advertisement'] = get_object_or_404(Advertisement, id=adv_id)

        # проверяем права на редактирование
        if not User.objects.get(id=request.user.id) == args['advertisement'].user:
            return redirect(args['advertisement'].adv_type.url, bicycle_id=adv_id)


        args['photos'] = Photo.objects.filter(advertisement = adv_id)
        for photo in args['photos']:
            print(photo.file_medium.url)
        args['username'] = request.user.username
        return render(request, 'photos/advertisement_photo_edit.html', args)

    def post(self, request, adv_id):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.advertisement_id = adv_id
            photo.save()

            # генерируем строку формы в js для удаления фотографии
            csrf_ = '<input name="csrfmiddlewaretoken" value="Q8R1TEKWHXTAYDeXDfIo1CxH102GR1M2Xds9JV61292z4XL3SN7L7LrjyssRFI3K" type="hidden">'#str(csrf(request))
            js_photo_delete = '<form method="post" action="/photos/advertisement/' + str(adv_id) + '/delete/' + str(photo.id) + '/">' + csrf_ + '<input type="hidden" name="next" value="' + request.path + '">' + '<button type="submit" class="btn btn-danger pull-right">' + '<span class="glyphicon glyphicon-trash"></span> Удалить фотографию' + '</button>' + '</form>'

            data = {'is_valid': True, 'url_small': photo.file_small.url, 'url': photo.file.url, 'js_photo_delete': js_photo_delete }
            # data = {'is_valid': True, 'url_small': photo.file_small.url, 'url': photo.file.url, 'photo_id': photo.id, 'adv_id': adv_id }
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
def clear_adv_photo(request, adv_id):
    for photo in Photo.objects.filter(advertisement = adv_id):
        # photo.file.delete()
        photo.delete()
    return redirect(request.POST.get('next'))

def delete_adv_photo(request, adv_id, photo_id):
    Photo.objects.filter(id = photo_id).delete()
    return redirect(request.POST.get('next'))
