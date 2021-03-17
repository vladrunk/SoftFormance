from django.contrib import admin

from .models import RegisteredUser, FeedItem


@admin.register(RegisteredUser)
class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = 'user', 'id',


@admin.register(FeedItem)
class FeedItemAdmin(admin.ModelAdmin):
    list_display = 'user', 'content',
