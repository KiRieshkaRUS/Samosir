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
        verbose_name = 'Фото мест размещений'
        verbose_name_plural = 'Фото мест размещений'


class Transport(models.Model):
    transport_name = models.CharField(max_length=250, verbose_name='Название транспорта', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    type = models.TextField(max_length=150, verbose_name='Тип', blank=True, null=True)
    speed = models.TextField(max_length=250, verbose_name='Время доставки', blank=True, null=True)
    price = models.TextField(max_length=150, verbose_name='Стоимость', blank=True, null=True)
    rate = models.TextField(max_length=150, verbose_name='Рейтинг', blank=True, null=True)
    transport_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.transport_name

    def get_absolute_url(self):
        return f'/transports/{self.transport_slug}'

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Траспорт'


class TransportPhoto(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, verbose_name='Транспорт')
    photo = models.ImageField(verbose_name='Фото', null=True, upload_to='media/transport_photo')

    def __str__(self):
        return self.transport.transport_name

    class Meta:
        verbose_name = 'Фото транспорта'
        verbose_name_plural = 'Фото транспорта'


class Fun(models.Model):
    fun_name = models.CharField(max_length=250, verbose_name='Название', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    type = models.TextField(max_length=150, verbose_name='Тип', blank=True, null=True)
    speed = models.TextField(max_length=250, verbose_name='Месторасположение', blank=True, null=True)
    price = models.TextField(max_length=150, verbose_name='Стоимость', blank=True, null=True)
    rate = models.TextField(max_length=150, verbose_name='Рейтинг', blank=True, null=True)
    fun_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.fun_name

    def get_absolute_url(self):
        return f'/funs/{self.fun_slug}'

    class Meta:
        verbose_name = 'Развлечение'
        verbose_name_plural = 'Развлечения'


class FunPhoto(models.Model):
    fun = models.ForeignKey(Fun, on_delete=models.CASCADE, verbose_name='Развлечение')
    photo = models.ImageField(verbose_name='Фото', null=True, upload_to='media/fun_photo')

    def __str__(self):
        return self.fun.fun_name

    class Meta:
        verbose_name = 'Фото развелчений'
        verbose_name_plural = 'Фото развелчений'

