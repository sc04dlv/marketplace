from django import forms
from .models import Bicycle, Ski
#
# class NameForm(forms.ModelForm):
#     class Meta:
#         model = Advertisement
#         fields = ['title', 'note', 'price']



class BicycleForm(forms.ModelForm):
    class Meta:
        model = Bicycle
        fields = ['title', 'note', 'price', 'ident', 'year', 'size', 'weight', 'bicycle_type']


class SkiForm(forms.ModelForm):
    class Meta:
        model = Ski
        fields = ['title', 'note', 'price', 'ident', 'year', 'size', 'weight', 'for_weight', 'ski_type']
