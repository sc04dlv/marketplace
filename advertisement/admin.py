# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

# from django.contrib.contenttypes.admin import TabularInline
from .models import Advertisement, Bicycle, Ski

# class AdvertisementAdmin(admin.Advertisement):
#     fields = ['title','note','price']

class BicycleInline(admin.TabularInline):  #StackedInline
    model = Bicycle

admin.site.register(Bicycle)
class AdvertisementAdmin(admin.ModelAdmin):
    # list_display = ('title', 'size', 'bicycle_types')
    inlines = [
        BicycleInline,
    ]

# admin.site.register(AdvertisementAdmin)

# Register your models here.
