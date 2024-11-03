from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    return render(request, 'main/index.html')


def my_projects(request):
    projects = Projects.objects.order_by('-date_added')

    context = {'projects': projects}

    return render(request, 'main/my_projects.html', context)


def project_view(request, project_slug):
    project = Projects.objects.get(project_slug=project_slug)

    context = {'project': project}

    return render(request, 'main/project.html', context)


@login_required(login_url='users:login')
def order_view(request):
    if request.method != 'POST':
        form = OrderForm()
    else:
        form = OrderForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.user = request.user
            form.save()
            send_mail('Заказ оформлен', f'Добрый день, {request.user.username}!\n'
                      f'Ваш заказ {new_order} успешно оформлен. Администратор сайта скоро свяжется с вами!',
                      settings.EMAIL_HOST_USER, [new_order.email])
            send_mail('Новый заказ', f'Добрый день!\nНа сайте оформлен заказ.'
                      f'\nПользователь: {request.user.username}\n'
                      f'Номер телефона: {new_order.phone_number}\n'
                      f'email: {new_order.email}\n'
                      f'Адрес доставки: {new_order.address}\n'
                      f'{new_order.theme}\n'
                      f'{new_order.description}', settings.EMAIL_HOST_USER,
                      ['kir300604@yandex.ru'])
            return redirect('main:ordered')

    context = {'form': form}
    return render(request, 'main/order.html', context)


@login_required(login_url='users:login')
def ordered(request):
    return render(request, 'main/ordered.html')