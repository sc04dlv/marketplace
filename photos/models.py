#coding: utf-8
from __future__ import unicode_literals

from django.db import models
from PIL import Image
from imagekit.models.fields import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill
from django.dispatch import receiver

import os
import datetime

from advertisement.models import Advertisement

def get_image_filename(instance, filename):
    now = datetime.datetime.now()
    str(now)
    # slug = instance.advertisement.id
    return "photos/%s/%s/%s/%s" % (now.year, now.month, now.day, filename)

class Photo(models.Model):
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        related_name='photos',
    )

    file = models.ImageField(upload_to=get_image_filename)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    file_small  = ImageSpecField(source='file',
                                  processors=[ResizeToFill(100, 100)],
                                  format='JPEG',
                                  options={'quality': 60})
    file_medium = ImageSpecField(source='file',
                                  processors=[ResizeToFill(200, 200)],
                                  format='JPEG',
                                  options={'quality': 60})
    file_big    = ImageSpecField(source='file',
                                  processors=[ResizeToFill(640, 480)],
                                  format='JPEG',
                                  options={'quality': 60})

@receiver(models.signals.pre_delete, sender=Photo, weak=False)
def delete_photo(sender, instance, **kwargs):
    path_to_photo = instance.file.path
    if os.path.exists(path_to_photo):
        os.remove(path_to_photo)

@receiver(models.signals.pre_delete, sender=Advertisement, weak=False)
def delete_photos_from_album(sender, instance, **kwargs):
    photos = Photo.objects.filter(advertisement=instance.id)
    for photo in photos:
        photo.delete()

# проверка прав доступа
# @receiver(models.signals.pre_save, sender=Photo, weak=False)
# def save_photo(sender, instance, **kwargs):
#     if not User.objects.get(id=request.user.id) == args['advertisement'].user:
#         return redirect(args['advertisement'].adv_type.url, bicycle_id=adv_id)
