from django.contrib import admin
from . import models


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'gender', 'age']
    list_display_links = ['username']
    search_fields = ['username']
    ordering = ['id']


admin.site.register(models.UserProfile, ProfilesAdmin)