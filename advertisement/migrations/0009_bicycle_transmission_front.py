# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-13 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0008_auto_20180510_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicycle',
            name='transmission_front',
            field=models.IntegerField(choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12')], default=3),
            preserve_default=False,
        ),
    ]
