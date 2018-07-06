# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from .models import Race, Milestone, Protocol, UserRaceLink
# from photos.models import Photo


admin.site.register(UserRaceLink)
admin.site.register(Protocol)

class MilestoneInline(admin.TabularInline):
    model = Milestone

class RaceAdmin(admin.ModelAdmin):
    inlines = [
        MilestoneInline,
    ]

admin.site.register(Race, RaceAdmin)
