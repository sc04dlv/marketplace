# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-13 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0010_auto_20180513_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='ident',
        ),
    ]
