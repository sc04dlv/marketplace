# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models.User import User
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

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

class Image(models.Model):
    image = models.ImageField(upload_to="media/image")

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

class Advertisement(models.Model):
    class Meta:
        abstract = True

    images = GenericRelation(Image)

    user_id = models.ForeignKey(
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




class Bicycle(Advertisement):
    # advertisement = models.ForeignKey(
    #     Advertisement,
    #     on_delete=models.CASCADE,
    #     related_name='bicycles'
    # )

    # advertisement = models.OneToOneField(Advertisement,
    #                                      on_delete=models.CASCADE,
    #                                      primary_key=True,)

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
