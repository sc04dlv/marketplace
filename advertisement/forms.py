from django import forms
from .models import Bicycle
#
# class NameForm(forms.ModelForm):
#     class Meta:
#         model = Advertisement
#         fields = ['title', 'note', 'price']



class BicycleForm(forms.ModelForm):
    class Meta:
        model = Bicycle
        fields = ['title', 'note', 'price', 'ident', 'year', 'size', 'weight', 'bicycle_type']
