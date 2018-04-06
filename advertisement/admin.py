# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from .models import Bicycle, Ski, BicycleType, BicycleJumper, Image
from django.contrib.contenttypes.admin import GenericTabularInline

# class AdvertisementAdmin(admin.Advertisement):
#     fields = ['title','note','price']

# class BicycleInline(admin.StackedInline):  #TabularInline
#     model = Bicycle#.advertisement.through
#     fk_name = 'advertisement'
#     extra = 1
#     max_num = 1
#     min_num = 1

    # exclude = ('title','user','note','ident','price','weight','year',)
# class SkiInline(admin.TabularInline):
#     model = Ski
#     fk_name = 'advertisement'

# class AdvertisementBicycleAdmin(admin.ModelAdmin):
#     inlines = [BicycleInline,]
#     exclude = ('title','user','note','ident','price','weight','year',)

# class AdvertisementSkiAdmin(admin.ModelAdmin):
#     inlines = [SkiInline,]


# admin.site.register(Advertisement, AdvertisementBicycleAdmin)

class ImageInline(GenericTabularInline):
    model = Image

class ImageAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Bicycle, ImageAdmin)
admin.site.register(Ski, ImageAdmin)


# admin.site.register(Bicycle)
# admin.site.register(Ski)

admin.site.register(BicycleType)
admin.site.register(BicycleJumper)


# Register your models here.
