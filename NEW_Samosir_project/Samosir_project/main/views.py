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


def transports(request):
    all_transports = Transport.objects.order_by('transport_name')

    context = {'all_transports': all_transports}

    return render(request, 'main/transports.html', context)


def transport_view(request, transport_slug):
    transport = Transport.objects.get(transport_slug=transport_slug)

    context = {'transport': transport}

    return render(request, 'main/transport.html', context)


def funs(request):
    all_funs = Fun.objects.order_by('fun_name')

    context = {'all_funs': all_funs}

    return render(request, 'main/funs.html', context)


def fun_view(request, fun_slug):
    fun = Fun.objects.get(fun_slug=fun_slug)

    context = {'fun': fun}

    return render(request, 'main/fun.html', context)