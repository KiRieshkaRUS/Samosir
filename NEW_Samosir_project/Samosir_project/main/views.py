from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'main/index.html')


def shelters(request):
    all_shelters = Shelter.objects.order_by('shelter_name')

    context = {'all_shelters': all_shelters}

    return render(request, 'main/shelters.html', context)


def shelter_view(request, shelter_slug):
    shelter = Shelter.objects.get(shelter_slug=shelter_slug)

    context = {'shelter': shelter}

    return render(request, 'main/shelter.html', context)