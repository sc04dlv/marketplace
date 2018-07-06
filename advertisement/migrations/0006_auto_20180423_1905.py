# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-23 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0005_auto_20180423_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisementtype',
            name='name',
        ),
        migrations.AddField(
            model_name='advertisementtype',
            name='url',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='adv_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.AdvertisementType'),
        ),
    ]