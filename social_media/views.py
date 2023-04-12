from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm
from django.contrib.auth.models import User
from .models import SocialProfile, Friend_Request
from django.db.models import Q
from django.views import View
from progress.utils import calculate_streak
from progress.models import workoutModel
from django.utils import timezone
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
    friendState=False
    a = SocialProfile.objects.get(user=request.user)
    b = SocialProfile.objects.get(user=User.objects.get(id=pk))
    #send friend request if not sent
    # remove friend if sent(sender=request.user) or accepted(either)
    # decline friend if sent(receiver = request.user)
    # accept friend request if sent(receiver= request.user)
    # checks if they are currently friends  
    fstatus=False
    #checks if I sent and pending
    Istatus=False
    #checks if other sent and pending
    pstatus=False
    #no relation
    nstatus=False
    g=False
    receiver= request.user
    sender = User.objects.get(id=pk)
    a = SocialProfile.objects.get(user=request.user)
    b = SocialProfile.objects.get(user=User.objects.get(id=pk))
    #if friends
    if(a.friends.filter(username=User.objects.get(id=pk)).exists()):
        fstatus=True
        
        if(request.method=="POST"):
            #delete friend
            if(len(Friend_Request.objects.filter(sender=request.user,receiver=User.objects.get(id=pk)))!=0):
                l= Friend_Request.objects.get(sender=request.user,receiver=User.objects.get(id=pk),status="accepted")
                l.delete()
                a.friends.remove(User.objects.get(id=pk))
                b.friends.remove(request.user)
                a.save()
                b.save()

            else:
                l=Friend_Request.objects.get(sender=User.objects.get(id=pk),receiver=request.user,status="accepted")
                l.delete()
                a.friends.remove(User.objects.get(id=pk))
                b.friends.remove(request.user)
                a.save()
                b.save()
            fstatus=False
    #if sent
    elif(len(Friend_Request.objects.filter(sender=request.user,receiver=User.objects.get(id=pk),status="sent"))!=0):
        Istatus=True
        g=True
        if request.method=="POST":
            Friend_Request.objects.get(sender=request.user,receiver=User.objects.get(id=pk),status="sent").delete()
            Istatus=False
    #if receiving   
    elif(len(Friend_Request.objects.filter(sender=User.objects.get(id=pk),receiver=request.user,status="sent"))!=0):
        pstatus=True
        g=True
        
        if(request.method == "POST"):
            #accept
            a=Friend_Request.objects.get(sender=User.objects.get(id=pk),receiver=request.user,status="sent")
            a.status="accepted"
            a.save()
            pstatus=False
    #if none, send
    else:
        nstatus=True
        if request.method=="POST":
            sender = request.user
            receiver = User.objects.get(id=pk)
            Friend_Request.objects.create(sender=sender, receiver=receiver, status='sent')
            nstatus=False

    # checks if friend request is currently sent
                

    if request.user.is_authenticated:
        profile= SocialProfile.objects.get(user_id=pk)
        context= {"fstatus":fstatus,"Istatus":Istatus,"pstatus":pstatus,"nstatus":nstatus,"profile":profile,"sender":sender,"receiver":receiver}  
        return render(request,'socialmedia/profiles.html',context)
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


    
def current_requests(request):
    receiver = request.user
    all_requests = Friend_Request.objects.filter(receiver=receiver,status="sent")
    return render(request,"socialmedia/requests.html",{"all_requests":all_requests})
def accept_requests(request, pk):
    receiver= request.user
    sender = User.objects.get(id=pk)
    curr_request =Friend_Request.objects.get(receiver=receiver,sender=sender,status='sent')
    if request.method == "POST":
        curr_request.status = "accepted"
        curr_request.save()
    return render(request,"#",{"curr_request":curr_request})

def friends(request):
    current_friends = SocialProfile.objects.get(user=request.user).friends.all()
    return render(request,"socialmedia/friends.html",{"current_friends":current_friends})


    # if send create a new object for
def friend_progress(request,pk):
    friend_status= False
    a = SocialProfile.objects.get(user=request.user)
    b = SocialProfile.objects.get(user=User.objects.get(id=pk))
    friend_journal_streak=0
    if(a.friends.filter(username=User.objects.get(id=pk)).exists()):
        friend_status=True

        friend_journal_streak = calculate_streak(user=User.objects.get(id=pk))



        data= workoutModel.objects.filter(user=request.user)
        user = request.user
        thirty_days_ago = timezone.now() - timezone.timedelta(days=30)

    # Get all the user's workouts in the last 30 days
        workouts = workoutModel.objects.filter(user=user, Date__gte=thirty_days_ago)
        totaltime=0
        for workout in workouts:
            totaltime+= workout.Duration_Hours
    # Count the number of workouts
        num_workouts = workouts.count()
        if(num_workouts!=0):
            time= totaltime/num_workouts
        else:
            time = 0
        time = round(time,2)
        #what to show:
        # show journal streak
        # workouts in the last 30 days
        #avg workout time

        context={'friend_journal_streak':friend_journal_streak,'time':time,"num_workouts":num_workouts,
                 "friend":b,"friend_status":friend_status}
    else:
        context={"friend":b,"friend_status":friend_status}
    return render(request,"socialmedia/friendprog.html",context)
