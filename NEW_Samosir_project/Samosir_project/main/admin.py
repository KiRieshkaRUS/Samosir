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

    get_html_photo.short_description = 'Фото мест раземещений'


class TransportsAdmin(admin.ModelAdmin):
    list_display = ['id', 'transport_name', 'type', 'price', 'transport_slug']
    list_display_links = ['transport_name']
    search_fields = ['transport_name']
    prepopulated_fields = {"transport_slug": ('transport_name', )}
    ordering = ['id']


class TransportPhotoAdmin(admin.ModelAdmin):
    list_display = ['transport', 'get_html_photo']
    list_display_links = ['transport']
    search_fields = ['transport']
    ordering = ['transport']
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        return mark_safe(f'<img src="{object.photo.url}", width="50">')

    get_html_photo.short_description = 'Фото транспорта'


class FunsAdmin(admin.ModelAdmin):
    list_display = ['id', 'fun_name', 'type', 'price', 'fun_slug']
    list_display_links = ['fun_name']
    search_fields = ['fun_name']
    prepopulated_fields = {"fun_slug": ('fun_name', )}
    ordering = ['id']


class FunPhotoAdmin(admin.ModelAdmin):
    list_display = ['fun', 'get_html_photo']
    list_display_links = ['fun']
    search_fields = ['fun']
    ordering = ['fun']
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        return mark_safe(f'<img src="{object.photo.url}", width="50">')

    get_html_photo.short_description = 'Фото развлечений'


admin.site.register(models.Shelter, SheltersAdmin)
admin.site.register(models.ShelterPhoto, ShelterPhotoAdmin)
admin.site.register(models.Transport, TransportsAdmin)
admin.site.register(models.TransportPhoto, TransportPhotoAdmin)
admin.site.register(models.Fun, FunsAdmin)
admin.site.register(models.FunPhoto, FunPhotoAdmin)
