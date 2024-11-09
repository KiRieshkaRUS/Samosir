from django.db import models


class UserProfile(models.Model):

    GENDER_CHOICES = (
        ('male', 'Мужчина'),
        ('female', 'Не мужчина'),
    )


    username = models.CharField(max_length=300, verbose_name='Имя пользователя')
    email = models.EmailField(verbose_name='Email')
    gender = models.CharField(max_length=150, choices=GENDER_CHOICES)
    birth = models.DateField(auto_now_add=False, auto_now=False)
    avatar = models.ImageField(upload_to='media/user_avatars', verbose_name='Аватар', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
