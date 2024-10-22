# Generated by Django 5.1.2 on 2024-10-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='data_added',
        ),
        migrations.AddField(
            model_name='projects',
            name='date_added',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата добавления'),
        ),
    ]
