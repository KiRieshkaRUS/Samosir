from django.contrib.auth.models import User
from django.db import models


class Projects(models.Model):
    project_name = models.CharField(max_length=250, verbose_name='Название проекта', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True, verbose_name='Дата добавления')
    price = models.FloatField(verbose_name='Цена', blank=True, null=True)
    project_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return f'/my_projects/{self.project_slug}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectPhoto(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name='Проект')
    photo = models.ImageField(verbose_name='Фото', null=True, upload_to='media/project_photo')

    def __str__(self):
        return self.project.project_name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Order(models.Model):
    theme = models.CharField(max_length=250, verbose_name='Тема')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    email = models.EmailField(max_length=100, verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=300, verbose_name='Номер телефона')
    address = models.CharField(max_length=300, verbose_name='Адрес доставки')
    description = models.TextField(verbose_name='Описание заказа')
    photo = models.ImageField(upload_to='media/orderPhotos', verbose_name='Фото',
                              null=True)

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

