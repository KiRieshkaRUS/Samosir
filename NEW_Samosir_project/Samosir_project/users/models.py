from django.db import models


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Мужчина'),
        ('F', 'Не мужчина'),
    )

    username = models.CharField(max_length=300, verbose_name='Имя пользователя')
    first_name = models.CharField(max_length=300, verbose_name='Имя')
    last_name = models.CharField(max_length=300, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    gender = models.CharField(verbose_name='Пол', choices=GENDER_CHOICES, blank=True, null=True)
    age = models.IntegerField(verbose_name='Возраст', blank=True, null=True)
    avatar = models.ImageField(upload_to='media/user_avatars', verbose_name='Аватар', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
