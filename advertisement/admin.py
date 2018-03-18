# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

# from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Advertisement, Bicycle, Ski

# class AdvertisementAdmin(admin.Advertisement):
#     fields = ['title','note','price']

class BicycleInline(admin.StackedInline):  #TabularInline
    model = Bicycle#.advertisement.through
    fk_name = 'advertisement'
    extra = 1
    max_num = 1
    min_num = 1
    # exclude = ('title','user','note','ident','price','weight','year',)
# class SkiInline(admin.TabularInline):
#     model = Ski
#     fk_name = 'advertisement'

class AdvertisementBicycleAdmin(admin.ModelAdmin):
    inlines = [BicycleInline,]
    exclude = ('title','user','note','ident','price','weight','year',)

# class AdvertisementSkiAdmin(admin.ModelAdmin):
#     inlines = [SkiInline,]


admin.site.register(Advertisement, AdvertisementBicycleAdmin)
# admin.site.register(Advertisement, AdvertisementSkiAdmin)

# Register your models here.
