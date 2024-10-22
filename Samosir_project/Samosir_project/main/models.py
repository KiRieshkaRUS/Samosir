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
