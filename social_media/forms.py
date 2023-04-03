from .models import SocialProfile, Friend_Request
from django import forms
from django.forms import ModelForm


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = SocialProfile
        fields = ['bio','profile_img']

class Friend_Request:
    class Meta: 
        pass   
#send request, create new data, sender is request.user, receiver is whoever page you are on
