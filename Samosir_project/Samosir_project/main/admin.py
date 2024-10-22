from django.contrib import admin
from . import models


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_name', 'date_added']
    list_display_links = ['project_name']
    search_fields = ['project_name']
    prepopulated_fields = {"project_slug": ('project_name', )}
    ordering = ['id', 'date_added']


admin.site.register(models.Projects, ProjectsAdmin)

