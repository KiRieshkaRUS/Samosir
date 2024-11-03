from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    theme = forms.CharField(max_length=250, label='Тема')
    email = forms.EmailField(max_length=100, label='Электронная почта')
    phone_number = forms.CharField(max_length=250, label='Номер телефона')
    address = forms.CharField(max_length=300, label='Адрес доставки')
    description = forms.Textarea()
    photo = forms.ImageField(label='Фото')

    class Meta:
        model = Order
        fields = ['theme', 'email', 'phone_number', 'address', 'description', 'photo']

