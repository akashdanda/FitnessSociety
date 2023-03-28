from django.shortcuts import render
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from social_media.models import SocialProfile
from .models import FriendRequest
from django.contrib.auth.decorators import login_required

@login_required
def send_friend_request(request, to_user_id):
    status=False
    from_user = request.user
    to_user = User.objects.get(id=to_user_id)
    friend_request = FriendRequest(from_user=from_user, to_user=to_user)
    friend_request.save()
    if friend_request:
        status =True
    context = {"status":status}
    return render(request,"hi",context)

@login_required
def accept_friend_request(request,requestID):
    FriendRequest = FriendRequest.objects.get(id=requestID)
    if FriendRequest.to_user == request.user:
        pass
        # add friends to both sides
