from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm
from django.contrib.auth.models import User

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
    return render(request,'socialmedia/socialprofile.html',{})
