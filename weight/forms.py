from django import forms
from .models import currentweight
class changeWeight(forms.ModelForm):
    class Meta:
        model=currentweight
        exclude = ['user','date']
