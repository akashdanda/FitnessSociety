from django.shortcuts import render, redirect
from .forms import addcalories,addworkouts, journalDaily
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import dailyJournal
from django.utils import timezone
from .models import workoutModel

from .utils import calculate_streak
# Create your views here.
@login_required
def calorieTrackerView(request):
    if request.method == "POST":
        form = addcalories(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user = request.user
            instance.save()

    else:
        form=addcalories()
    return render(request, 'progress/tracker.html',{"form":form})

@login_required
def progresshome(request):
    return render(request, "progress/progress_home.html",{})

@login_required
def workoutprogress(request):
    if request.method == 'POST':
        form= addworkouts(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user= request.user 
            instance.save()
            return redirect("graphs/")
    else:
        form = addworkouts()
    return render(request,'progress/workoutProg.html',{"form":form})

@login_required
def journals(request):
        
    if request.method == "POST":
        form = journalDaily(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user=request.user
            instance.save()
    else:
        form = journalDaily()
    return render(request,'progress/journals/journals.html',{"form":form})
@login_required
def alljournals(request):
    user = request.user
    streak = calculate_streak(user)
    all_journals = dailyJournal.objects.filter(user=request.user)
    return render(request,'progress/journals/AllJournals.html',{'all_journals':all_journals,"streak":streak})





