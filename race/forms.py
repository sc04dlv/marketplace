# -*- coding: utf-8 -*-

from django import forms
from .models import Protocol, Milestone, Race, UserRaceLink
from django.forms import Textarea

class ProtocolForm(forms.ModelForm):
    class Meta:
        model = Protocol
        fields = '__all__'
        # widgets = {
        #     'note': Textarea(attrs={'cols': 80, 'rows': 10}),
        # }

class UserRaceLinkForm(forms.ModelForm):
    class Meta:
        model = UserRaceLink
        fields = '__all__'
