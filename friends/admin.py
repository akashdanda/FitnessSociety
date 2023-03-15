from django.contrib import admin
from .models import FriendRequest, FriendsList
admin.site.register(FriendsList)
admin.site.register(FriendRequest)
