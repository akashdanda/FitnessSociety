from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm
from django.contrib.auth.models import User
from .models import SocialProfile
# Create your views here.
@login_required
def Profileviewupt(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.socialprofile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.socialprofile)
    context={'p_form':p_form}
    return render(request,'socialmedia/socialprofileUpt.html',context)
@login_required
def Profileview(request):
    print(request.user.id)
    return render(request,'socialmedia/socialprofile.html',{})

def profile(request,pk):

    if request.user.is_authenticated:
        profile= SocialProfile.objects.get(user_id=pk)
        return render(request,'socialmedia/profiles.html',{"profile":profile})
    else:
        return redirect('home')

def profile_list(request):
    if request.user.is_authenticated:
        profiles= SocialProfile.objects.exclude(user=request.user)

        return render(request,'socialmedia/profile_list.html',{"profiles":profiles})
    else:
        redirect('home')