from django.shortcuts import render, redirect
from .models import currentweight
from .forms import changeWeight
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def weight(request):
    if request.method == "POST":
        form = changeWeight(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect('weight_progress/')
    else:
        form = changeWeight()
    return render(request,'weight.html',{"form":form})

def line_graph(request):

    weights = currentweight.objects.filter(user=request.user)

    return render(request, 'studbud/weightgraph.html',{'weights':weights})
