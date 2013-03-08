from django.contrib import admin
from models import User, OAuthToken, Like, Friend

class UserAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'facebook_id', 'authorized', 'created_at', 'last_seen_at']

class OAuthTokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'issued_at', 'expires_at', 'expired']

admin.site.register(User, UserAdmin)
admin.site.register(OAuthToken, OAuthTokenAdmin)


class FriendAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'friend_of',
        'facebook_id'
    ]

admin.site.register(Friend, FriendAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'like_id',
        'facebook_user'
    ]

admin.site.register(Like, LikeAdmin)
