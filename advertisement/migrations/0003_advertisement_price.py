# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_advertisement_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]