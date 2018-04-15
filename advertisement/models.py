# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models.User import User
from django.contrib.auth.models import User
from django.conf import settings

# работа с изображением
from PIL import Image
from imagekit.models.fields import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill

# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.fields import GenericRelation
import datetime


class BicycleType(models.Model):
    code = models.CharField(max_length=20,)
    name = models.CharField(max_length=40,)

    def __str__(self):
      return ' '.join([
          self.name,
      ])

class BicycleJumper(models.Model):
    code = models.CharField(max_length=20,)
    name = models.CharField(max_length=40,)

    def __str__(self):
      return ' '.join([
          self.name,
      ])


class Advertisement(models.Model):
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
    )

    title = models.CharField(
        max_length=255,
    )

    note = models.CharField(
        max_length=4000,
    )

    date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    price = models.IntegerField()
    ident = models.IntegerField(blank = True, null=True,)
    weight = models.IntegerField(blank = True,)
    year = models.IntegerField(blank = True,)

    def __str__(self):
      return ' '.join([
          self.title,
          self.note,
          # self.price,
      ])

def get_image_filename(instance, filename):
    # title = instance.advertisement.id
    # slug = slugify(title)
    now = datetime.datetime.now()
    str(now)
    slug = instance.advertisement.id
    return "images/%s/%s/%s/%s-%s" % (now.year, now.month, now.day, slug, filename)

class Images(models.Model):
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(upload_to=get_image_filename, #'media/image',
                              verbose_name='Image',)
    image_small  = ImageSpecField(source='image',
                                  processors=[ResizeToFill(100, 100)],
                                  format='JPEG',
                                  options={'quality': 60})
    image_medium = ImageSpecField(source='image',
                                  processors=[ResizeToFill(200, 200)],
                                  format='JPEG',
                                  options={'quality': 60})
    image_big    = ImageSpecField(source='image',
                                  processors=[ResizeToFill(640, 480)],
                                  format='JPEG',
                                  options={'quality': 60})

    # def resize_image(self
    #                 ,width=None
    #                 ,height=None):
    #     original_image = Image.open(self.image)#input_image_path)
    #     w, h = original_image.size
    #     # print('The original image size is {wide} wide x {height} '
    #     #       'high'.format(wide=w, height=h))
    #
    #     if width and height:
    #         max_size = (width, height)
    #     elif width:
    #         max_size = (width, h)
    #     elif height:
    #         max_size = (w, height)
    #     else:
    #         # No width or height specified
    #         raise RuntimeError('Width or height required!')
    #
    #     original_image.thumbnail(max_size, Image.ANTIALIAS)
    #     original_image.save('images/2018/4/8/test.jpg')#output_image_path)
    #
    #     scaled_image = Image.open('images/2018/4/8/test.jpg')#output_image_path)
    #     width, height = scaled_image.size
    #     print('The scaled image size is {wide} wide x {height} '
    #           'high'.format(wide=width, height=height))
    #
    #

class Bicycle(Advertisement):
    # class Meta(Advertisement.Meta):
    #     verbose_name = test''

    size = models.IntegerField()

    # bicycle_types = (
    #     ('rigid',       'ригид'),
    #     ('hardtail',    'хардтейл'), #hardtail
    #     ('dvuhpodves',  'двухподвес'), #full_suspension
    #     ('city',        'городской'),
    #     ('road',        'шоссейный'),
    #     ('track',       'трековый'),
    #     ('children',    'детский'),
    #     ('bmx',         'BMX'),
    #     ('skladnoj',    'складной'), #folding
    # )
    # bicycle_type = models.CharField(max_length=20,
    #                                 choices=bicycle_types,
    #                                )

    bicycle_type = models.ForeignKey(
        BicycleType,
        related_name='bicycle_type',
    )

    jumper_front = models.ForeignKey(
        BicycleJumper,
        related_name='jumper_front',
        blank=True,
        null=True,
    )

    jumper_back = models.ForeignKey(
        BicycleJumper,
        related_name='jumper_back',
        blank=True,
        null=True,
    )


class Ski(Advertisement):
    size = models.IntegerField()
    for_weight = models.IntegerField(blank = True,)

    ski_types = (
        ('classic',  'классические'),
        ('skate',    'коньковые'),
        ('children', 'детские'),
    )

    ski_type = models.CharField(max_length=20,
                                choices=ski_types,
                               )
