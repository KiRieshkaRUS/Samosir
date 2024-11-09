from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


class SheltersAdmin(admin.ModelAdmin):
    list_display = ['id', 'shelter_name', 'type', 'price', 'shelter_slug']
    list_display_links = ['shelter_name']
    search_fields = ['shelter_name']
    prepopulated_fields = {"shelter_slug": ('shelter_name', )}
    ordering = ['id']


class ShelterPhotoAdmin(admin.ModelAdmin):
    list_display = ['shelter', 'get_html_photo']
    list_display_links = ['shelter']
    search_fields = ['shelter']
    ordering = ['shelter']
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        return mark_safe(f'<img src="{object.photo.url}", width="50">')

    get_html_photo.short_description = 'Фото'


admin.site.register(models.Shelter, SheltersAdmin)
admin.site.register(models.ShelterPhoto, ShelterPhotoAdmin)
