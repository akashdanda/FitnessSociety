from django.shortcuts import render
from progress.models import workoutModel
from django.views.generic import TemplateView
from django.utils import timezone
# Create your views here.

def workoutview(request):
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
    context={"data":data, "num_workouts":num_workouts,"time":time}
    return render(request,'studbud/graph.html',context)
def graphNavPage(request):

    return render(request,"studbud/graphNavigation.html")