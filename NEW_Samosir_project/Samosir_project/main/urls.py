from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('shelters', views.shelters, name='all_shelters'),
    path('shelters/<slug:shelter_slug>', views.shelter_view, name='shelter'),
    path('transports', views.transports, name='all_transports'),
    path('transports/<slug:transport_slug>', views.shelter_view, name='transport'),
    path('funs', views.funs, name='all_funs'),
    path('funs/<slug:fun_slug>', views.fun_view, name='fun')
]
