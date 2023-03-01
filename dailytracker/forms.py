from django.forms import ModelForm
from .models import DailyTracker


class TrackerForm(ModelForm):
    class Meta:
        model=DailyTracker
        fields= ['exercise','type','duration_in_hours']
        