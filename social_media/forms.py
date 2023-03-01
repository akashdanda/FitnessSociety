from .models import SocialProfile
from django import forms
from django.forms import ModelForm


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = SocialProfile
        fields = ['bio','profile_img']