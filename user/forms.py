# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# from django.forms import Textarea
# from django.forms import modelformset_factory
# from django.forms.models import inlineformset_factory


class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(label = "Email")
    # first_name = forms.CharField(label = "First name")
    # last_name = forms.CharField(label = "Last name")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")

    # def save(self, commit=True):
    #     user = super(CustomUserCreationForm, self).save(commit=False)
    #     user.first_name = first_name
    #     user.last_name = last_name
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user
