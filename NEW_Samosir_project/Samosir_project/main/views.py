from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'main/index.html')


def shelters(request):
    all_shelters = Shelter.objects.order_by('shelter_name')
    photos = ShelterPhoto.objects.filter()
    context = {'all_shelters': all_shelters, 'photos': photos}

    return render(request, 'main/shelters.html', context)


def shelter_view(request, shelter_slug):
    shelter_obj = Shelter.objects.get(shelter_slug=shelter_slug)
    photos = ShelterPhoto.objects.filter(shelter=shelter_obj)
    context = {'shelter': shelter_obj, 'photos': photos}

    return render(request, 'main/shelter.html', context)


def transports(request):
    all_transports = Transport.objects.order_by('transport_name')
    photos = TransportPhoto.objects.filter()
    context = {'all_transports': all_transports, 'photos': photos}

    return render(request, 'main/transports.html', context)


def transport_view(request, transport_slug):
    transport_obj = Transport.objects.get(transport_slug=transport_slug)
    photos = TransportPhoto.objects.filter(shelter=transport_obj)
    context = {'transport': transport_obj, 'photos': photos}

    return render(request, 'main/transport.html', context)


def funs(request):
    all_funs = Fun.objects.order_by('fun_name')
    photos = TransportPhoto.objects.filter()
    context = {'all_funs': all_funs, 'photos': photos}

    return render(request, 'main/funs.html', context)


def fun_view(request, fun_slug):
    fun_obj = Fun.objects.get(fun_slug=fun_slug)
    photos = FunPhoto.objects.filter(shelter=fun_obj)

    context = {'fun': fun_obj, 'photos': photos}

    return render(request, 'main/fun.html', context)