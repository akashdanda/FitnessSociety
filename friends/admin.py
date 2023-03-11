from django.contrib import admin
from .models import FriendRequest, FriendsList

# Register your models here.
class FriendListAdmin(admin.ModelAdmin):
    list_filter=['user']
    list_display= ['user']
    search_fields = ['user']
    readonly_fields = ['user']

    class Meta:
        model = FriendsList
admin.site.register(FriendsList, FriendListAdmin)

class FriendRequestAdmin(admin.ModelAdmin):
    list_filter=['sender','receiver']
    list_display = ['sender','receiver']
    search_fields=['sender__username','sender__email','receiver__email'
                   ,'receiver__username']
    class Meta:
        model= FriendRequest
admin.site.register(FriendRequest, FriendRequestAdmin)
