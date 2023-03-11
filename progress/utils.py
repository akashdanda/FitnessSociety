from django.utils import timezone
from datetime import timedelta
from .models import dailyJournal
def calculate_streak(user):
    journals = dailyJournal.objects.filter(user=user).order_by('-today')
    current_streak = 0
    for i, journal in enumerate(journals):
        if i == 0:
            current_date = timezone.now().date()
        else:
            current_date = journals[i-1].today

        if journal.today == current_date:
            current_streak += 1
        else:
            break

    return current_streak
