from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class SocialProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,default=User)
    bio = models.TextField(blank=True)
    id = models.BigAutoField(primary_key=True)
    friends = models.ManyToManyField(User, related_name='friends',blank=True)
    profile_img= models.ImageField(upload_to='static/images/profile_images',default="static/images/profile_images/blankProfile.png")
    def get_friends(self):
        return self.friends.all()
    def num_of_friends(self):
        return self.friends.all().count()
  

def create_profile(sender,instance,created, **kwargs):
    if created:
        user_profile = SocialProfile(user=instance)
        user_profile.save()


post_save.connect(create_profile,sender=User)
CHOICES= [('sent','sent'),
          ('accepted','accepted'),
          ('unfriend','unfriend')]
class Friend_Request(models.Model):
    sender = models.ForeignKey(User,related_name='sender',on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name="receiver",on_delete=models.CASCADE)
    status = models.CharField(max_length=8,choices=CHOICES,null=True)

    
@receiver(post_save,sender=Friend_Request)
def friend_status(sender,instance, **kwargs):
    sender = instance.sender
    receiver = instance.receiver 
    if(instance.status=='accepted'):
        SocialProfile.objects.get(user=sender).friends.add(receiver)
        SocialProfile.objects.get(user=receiver).friends.add(sender)    