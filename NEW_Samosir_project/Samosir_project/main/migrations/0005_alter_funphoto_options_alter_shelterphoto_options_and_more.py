# Generated by Django 5.1.3 on 2024-11-15 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_fun_transport_funphoto_transportphoto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funphoto',
            options={'verbose_name': 'Фото развелчений', 'verbose_name_plural': 'Фото развелчений'},
        ),
        migrations.AlterModelOptions(
            name='shelterphoto',
            options={'verbose_name': 'Фото мест размещений', 'verbose_name_plural': 'Фото мест размещений'},
        ),
        migrations.AlterModelOptions(
            name='transportphoto',
            options={'verbose_name': 'Фото транспорта', 'verbose_name_plural': 'Фото транспорта'},
        ),
    ]