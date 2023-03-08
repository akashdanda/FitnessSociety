from django import forms
from .models import calorieTracker,workoutModel, dailyJournal
class addcalories(forms.ModelForm):
    class Meta:
        model=calorieTracker
        exclude = ['user']

class addworkouts(forms.ModelForm):
    class Meta:
        model=workoutModel
        exclude = ['user']

class journalDaily(forms.ModelForm):
    Upload_Journal = forms.CharField(widget=forms.Textarea, label='',initial="Record any thoughts.")
    class Meta:
        model = dailyJournal
        fields = ['Upload_Journal']
    