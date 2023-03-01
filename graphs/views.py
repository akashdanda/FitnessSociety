from django.shortcuts import render
from progress.models import workoutModel
from django.views.generic import TemplateView
# Create your views here.

def workoutview(request):
    data= workoutModel.objects.filter(user=request.user)
    context={"data":data}
    return render(request,'studbud/graph.html',context)
def graphNavPage(request):

    return render(request,"studbud/graphNavigation.html")