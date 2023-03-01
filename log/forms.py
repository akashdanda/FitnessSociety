from django.contrib.auth.forms import UserCreationForm,SetPasswordForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password1','password2']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model=User
        fields=['new_password1','new_password2']
