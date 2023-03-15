from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='friend_requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='friend_requests_received', on_delete=models.CASCADE)

class FriendsList(models.Model):
    user= models.ForeignKey(User,related_name='friends' ,on_delete=models.CASCADE)
    friends = models.ManyToManyField(User,related_name='friend_of',blank=True)