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
    all_journals= reversed(all_journals)
    return render(request,'progress/journals/AllJournals.html',{'all_journals':all_journals,"streak":streak})

def my_streak(request):
    user=request.user
    journal_streak= calculate_streak(user)
    data= workoutModel.objects.filter(user=request.user)
    user = request.user
    thirty_days_ago = timezone.now() - timezone.timedelta(days=30)

    # Get all the user's workouts in the last 30 days
    workouts = workoutModel.objects.filter(user=user, Date__gte=thirty_days_ago)
    data=workouts
    totaltime=0
    for workout in workouts:
        totaltime+= workout.Duration_Hours
    # Count the number of workouts
    num_workouts = workouts.count()
    time=0
    if(num_workouts>0):
        time= totaltime/num_workouts
    time = round(time,2)
    context={"journal_streak":journal_streak ,"num_workouts":num_workouts,"time":time}
    return render(request,"progress/streak.html",context)