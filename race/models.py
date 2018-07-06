# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.conf import settings

from django.db import models

class Race(models.Model):
    title = models.CharField(
        max_length=80,
    )

    note = models.CharField(
        max_length=4000,
    )

    begin_date = models.DateTimeField()

    def __str__(self):
      return ' '.join([
          self.title,
      ])

class Milestone(models.Model):

    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=80,
    )

    def __str__(self):
      return ' '.join([
          self.title,
      ])

class Protocol(models.Model):
# дописать уникальность - user, race, milestone

    # class Meta:
        # verbose_name = ''
        # verbose_name_plural = ''

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
    )

    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
    )

    milestone = models.ForeignKey(
        Milestone,
        on_delete=models.CASCADE,
        related_name='protocols',
    )

    date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    unique_together = ('user', 'milestone', 'race')

    def __str__(self):
      return ' '.join([
          # self.user,
          self.milestone.title,
          # self.date
      ])

class UserRaceLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
