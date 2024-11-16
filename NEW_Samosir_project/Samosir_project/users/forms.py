from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=250, label='Имя пользователя')
    first_name = forms.CharField(max_length=100, label='Имя')
    last_name = forms.CharField(max_length=100, label='Фамилия')
    email = forms.EmailField(max_length=100, label='Электронная почта')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот адрес электронной почты уже занят!")
        return email

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Мужчина'),
        ('F', 'Не мужчина'),
    )

    username = forms.CharField(max_length=250, label='Имя пользователя', required=True)
    first_name = forms.CharField(max_length=100, label='Имя', required=True)
    last_name = forms.CharField(max_length=100, label='Фамилия', required=True)
    email = forms.EmailField(max_length=100, label='Электронная почта', required=True)
    gender = forms.ChoiceField(label='Пол', choices=GENDER_CHOICES)
    age = forms.IntegerField(label='Возраст', required=True)
    avatar = forms.ImageField(label='media/user_avatars', required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'age']

