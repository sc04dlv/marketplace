# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-08 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_auto_20180408_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ski',
            name='bicycle_type',
        ),
        migrations.AddField(
            model_name='ski',
            name='ski_type',
            field=models.CharField(choices=[(b'classic', b'\xd0\xba\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8\xd0\xb5'), (b'skate', b'\xd0\xba\xd0\xbe\xd0\xbd\xd1\x8c\xd0\xba\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb5'), (b'children', b'\xd0\xb4\xd0\xb5\xd1\x82\xd1\x81\xd0\xba\xd0\xb8\xd0\xb5')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]