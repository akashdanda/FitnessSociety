from django.shortcuts import render

# Create your views here.
from .models import DailyTracker
from .forms import TrackerForm
from django.contrib.auth.decorators import login_required

@login_required
def trackerview(request):
    form = TrackerForm
    if request.method=='POST':
        form=TrackerForm(request.POST)
        if form.is_valid():
            n=form.cleaned_data['']
            form.save()
    context={'form':form}
    return render(request, 'tracker.html',context)