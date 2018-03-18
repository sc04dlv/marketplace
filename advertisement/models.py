# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.auth.models.User import User
from django.conf import settings


class Advertisement(models.Model):
    # class Meta:
    #     abstract = True

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=255,
    )

    note = models.CharField(
        max_length=4000,
    )

    date = models.DateTimeField(
        auto_now_add=True,
    )

    price = models.IntegerField()
    ident = models.IntegerField(blank = True,)
    weight = models.IntegerField(blank = True,)
    year = models.IntegerField(blank = True,)

    def __str__(self):
      return ' '.join([
          self.title,
          self.note,
      ])

class Bicycle(Advertisement):
    # advertisement = models.ForeignKey(
    #     Advertisement,
    #     on_delete=models.CASCADE,
    #     related_name='bicycles'
    # )
    advertisement = models.OneToOneField(Advertisement)

    size = models.IntegerField()

    bicycle_types = (
        ('rigid',       'ригид'),
        ('hardtail',    'хардтейл'), #hardtail
        ('dvuhpodves',  'двухподвес'), #full_suspension
        ('city',        'городской'),
        ('road',        'шоссейный'),
        ('track',       'трековый'),
        ('children',    'детский'),
        ('bmx',         'BMX'),
        ('skladnoj',    'складной'), #folding
    )
    bicycle_type = models.CharField(max_length=20,
                                    choices=bicycle_types,
                                   )


class Ski(Advertisement):
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        related_name='skis'
    )

    size = models.IntegerField()
    for_weight = models.IntegerField(blank = True,)

    ski_types = (
        ('classic', 'классические'),
        ('skate','коньковые'),
        ('children','детские'),
    )
    ski_type = models.CharField(max_length=20,
                                choices=ski_types,
                               )

# Create your models here.
