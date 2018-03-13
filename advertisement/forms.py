from django import forms
from .models import Advertisement

class NameForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        # title = forms.CharField(label='Name', max_length=100)
        # note = forms.CharField(widget=forms.Textarea)
        # price = forms.IntegerField()
        fields = ['title', 'note', 'price']
