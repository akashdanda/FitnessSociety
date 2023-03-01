from django.contrib import admin
from .models import calorieTracker,workoutModel, dailyJournal
# Register your models here.
admin.site.register(calorieTracker)
admin.site.register(workoutModel)
admin.site.register(dailyJournal)
