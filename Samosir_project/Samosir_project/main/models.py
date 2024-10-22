from django.db import models

class Projects(models.Model):
    project_name = models.CharField(max_length=250, verbose_name='Название проекта',
                                    blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    data_added = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    price = models.FloatField(verbose_name='Цена', blank=True, null=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

