from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('shelters', views.shelters, name='all_shelters'),
    path('shelters/<slug:shelter_slug>', views.shelter_view, name='shelter')
]
