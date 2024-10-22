from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'main/index.html')


def my_projects(request):
    projects = Projects.objects.order_by('-date_added')

    context = {'projects': projects}

    return render(request, 'main/my_projects.html', context)