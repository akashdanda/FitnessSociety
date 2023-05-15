from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.views import View
from progress.utils import calculate_streak
from progress.models import workoutModel
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request, 'home.html')

def information(request):
    logged_in=False
    logged_out=False
    if(request.user.is_authenticated):
        logged_in=True

    else:
        logged_out=True
    return render(request, 'information.html',{"login":logged_in,"logout":logged_out})

def test(request):
    return render(request, 'test.html',{})
    
def nav(request):
    return render(request, 'navigation_page.html',{})