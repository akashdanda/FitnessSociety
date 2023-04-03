from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm
from django.contrib.auth.models import User
from .models import SocialProfile, Friend_Request
from django.db.models import Q
from django.views import View
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
    profile = SocialProfile.objects.get(user=request.user)
    context ={'profile':profile}
    print(request.user.id)
    return render(request,'socialmedia/socialprofile.html',context)

@login_required
def profile(request,pk):
    receiver=''
    sender=''
    state=True
    if(len(Friend_Request.objects.filter(sender=request.user,receiver=User.objects.get(id=pk),status="sent"))!=0):
        state=False
        curr_req= Friend_Request.objects.filter(sender=request.user,receiver=User.objects.get(id=pk),status="sent")
        if request.method=="POST":
            if(curr_req[0].status=="sent"):
                pass
                
    else:    
        if request.method=="POST":
            sender = request.user
            receiver = User.objects.get(id=pk)
            Friend_Request.objects.create(sender=sender, receiver=receiver, status='sent')

    if request.user.is_authenticated:
        profile= SocialProfile.objects.get(user_id=pk)
        return render(request,'socialmedia/profiles.html',{"profile":profile,"receiver":receiver,"sender":sender,"state":state})
    else:
        return redirect('home')


def profile_search_results(request):
    return render(request, "socialmedia/profile_list.html",{})

def profile_search_bar(request):
    context={}
    query_dict = request.GET
    query = query_dict.get("query")
    context= {"query":query}
    user_profiles = None
    if query is not None:
        user_profiles = User.objects.filter(username__icontains=query).distinct()
        accounts=[]
        for user in user_profiles:
            accounts.append(user)
        context['accounts'] = accounts
    return render(request, "socialmedia/Search.html",context)

def decline_cancel_request(request,userID):
    receiver = User.objects.get(id=userID)
    sender= request.user
    Friend_Request.objects.delete(sender=sender,receiver=receiver, status='sent')
    return render(request,"",{})


    

def accept_requests(request, userID):
    receiver= request.user
    all_requests= Friend_Request.objects.filter(receiver=receiver,status='sent')
    sender = User.objects.get(id=userID)
    curr_request =Friend_Request.objects.get(receiver=receiver,sender=sender,status='sent')
    if request.method == "POST":
        curr_request.status = "accepted"
        curr_request.save()
    return render(request,"socialmedia/requests.html",{"curr_request":curr_request,"all_requests":all_requests})

def friends(request):
    current_friends = SocialProfile.objects.get(user=request.user).friends.all()
    return render(request,"socialmedia/friends.html",{"current_friends":current_friends})


    # if send create a new object for
