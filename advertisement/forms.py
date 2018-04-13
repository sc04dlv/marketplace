# -*- coding: utf-8 -*-

from django import forms
from .models import Advertisement, Bicycle, Ski, BicycleType, BicycleJumper, Images
from django.forms import Textarea
from django.forms import modelformset_factory
from django.forms.models import inlineformset_factory

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Images
        fields = ('image', )
        # widget=forms.FileInput(attrs={'multiple': 'multiple'})

ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3, can_delete=True)
# ImageFormset = inlineformset_factory(Advertisement, Images, fields = '__all__')


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = '__all__'
        widgets = {
            'note': Textarea(attrs={'cols': 80, 'rows': 10}),
        }


class BicycleForm(forms.ModelForm):
    class Meta(AdvertisementForm.Meta):
        model = Bicycle


class SkiForm(forms.ModelForm):
    class Meta(AdvertisementForm.Meta):
        model = Ski


class BaseFilterForm(forms.Form):
    price_min   = forms.IntegerField(label="Цена с"  ,required=False)
    price_max   = forms.IntegerField(label="Цена по"  ,required=False)

    weight_min  = forms.IntegerField(label="Вес с" ,required=False)
    weight_max  = forms.IntegerField(label="Вес по" ,required=False)

    # title_like  = forms.CharField(label="title_like"    ,required=False)
    # note_like   = forms.CharField(label="note_like"     ,required=False)
    # date_min    = forms.DateTimeField(label="date_min"  ,required=False)
    # date_max    = forms.DateTimeField(label="date_max"  ,required=False)
    # year_min    = forms.IntegerField(label="year_min"   ,required=False)
    # year_max    = forms.IntegerField(label="year_max"   ,required=False)

class BicycleFilterForm(BaseFilterForm):
    # bicycle_type = forms.CharField(label="bicycle_type" ,required=False)
    bicycle_type = forms.ModelMultipleChoiceField(queryset=BicycleType.objects.all(),
                                                  required=False,
                                                  widget=forms.CheckboxSelectMultiple,
                                                  label="Тип велосипеда",)
    jumper_front = forms.ModelMultipleChoiceField(queryset=BicycleJumper.objects.all(),
                                                  required=False,
                                                  widget=forms.CheckboxSelectMultiple,
                                                  label="Переключатель передний",)
    jumper_back =  forms.ModelMultipleChoiceField(queryset=BicycleJumper.objects.all(),
                                                  required=False,
                                                  widget=forms.CheckboxSelectMultiple,
                                                  label="Переключатель задний",) #(attrs={'class': 'form-control'}),)




# class BicycleFilterForm_Test(forms.ModelForm):
#     price_min   = forms.IntegerField(label="price_min"  ,required=False)
#     price_max   = forms.IntegerField(label="price_max"  ,required=False)
#     weight_min  = forms.IntegerField(label="weight_min" ,required=False)
#     weight_max  = forms.IntegerField(label="weight_max" ,required=False)
#
#     class Meta:
#         model = Bicycle
#         fields = ['bicycle_type']
