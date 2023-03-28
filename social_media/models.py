from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
# Create your models here.
class SocialProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,default=User)
    bio = models.TextField(blank=True)
    id = models.BigAutoField(primary_key=True)
    profile_img= models.ImageField(upload_to='static/images/profile_images',default="static/images/profile_images/blankProfile.png")
    def __str__(self):
        return f'{self.user.username} Profile'

def create_profile(sender,instance,created, **kwargs):
    if created:
        user_profile = SocialProfile(user=instance)
        user_profile.save()


post_save.connect(create_profile,sender=User)


