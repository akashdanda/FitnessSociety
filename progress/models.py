from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class calorieTracker(models.Model):
    user= models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    current= models.IntegerField(default=0)
    target = models.IntegerField(default=0)
TypeOptions=[('CARDIO','cardio'),('STRENGTH TRAINING','strength training'),('FLEXIBILITY','flexibility'),('MUSCULAR ENDURANCE','muscular endurance')]
MoodOptions=[("ENERGIZED",'energized'),('EXCITED','excited'),("FATIGUED",'fatigued'),('STRESSED', 'stressed'),('CALM','calm'),('SAD','sad')]

class workoutModel(models.Model):
    user= models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    Quick_Description=models.TextField(max_length=100,null=True)
    Date= models.DateField(auto_now=True)
    Duration_Hours=models.PositiveIntegerField(null=True)
    Exercise_Category=models.CharField(max_length=18,choices=TypeOptions)
    Mood=models.CharField(max_length=9,choices=MoodOptions)
    
    def __str__(self):
        return "{}".format(self.user)

class dailyJournal(models.Model):
    user= models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    Upload_Journal = models.TextField(default="Record how you are feeling.")
    today= models.DateField(default=now)
    @property
    def username(self):
        return self.user.username
        
