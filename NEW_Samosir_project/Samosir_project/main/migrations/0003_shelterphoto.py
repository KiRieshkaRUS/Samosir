# Generated by Django 5.1.3 on 2024-11-09 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_shelter_shelter_slug_alter_shelter_placement_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShelterPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='media/shelter_photo', verbose_name='Фото')),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shelter', verbose_name='Место размещения')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
    ]