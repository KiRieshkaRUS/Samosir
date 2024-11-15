from django.db import models


class Shelter(models.Model):
    shelter_name = models.CharField(max_length=250, verbose_name='Название места', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    type = models.TextField(max_length=150, verbose_name='Тип', blank=True, null=True)
    placement = models.TextField(max_length=250, verbose_name='Месторасположение', blank=True, null=True)
    price = models.TextField(max_length=150, verbose_name='Стоимость за сутки', blank=True, null=True)
    rate = models.TextField(max_length=150, verbose_name='Рейтинг', blank=True, null=True)
    shelter_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.shelter_name

    def get_absolute_url(self):
        return f'/shelters/{self.shelter_slug}'

    class Meta:
        verbose_name = 'Место размещения'
        verbose_name_plural = 'Места размещений'


class ShelterPhoto(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, verbose_name='Место размещения')
    photo = models.ImageField(verbose_name='Фото', null=True, upload_to='media/shelter_photo')

    def __str__(self):
        return self.shelter.shelter_name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


