from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class currentweight(models.Model):
    user= models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    cur_weight = models.DecimalField(decimal_places=3,max_digits=7)
    date = models.DateField(null=True)
    def __str__(self):
        return "{}".format(self.user)