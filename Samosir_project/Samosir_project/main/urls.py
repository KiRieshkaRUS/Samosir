from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('my_projects', views.my_projects, name='projects'),
    path('my_projects/<slug:project_slug>', views.project_view, name='project'),
    path('order/', views.order_view, name='order'),
    path('ordered/', views.ordered, name='ordered')
]
