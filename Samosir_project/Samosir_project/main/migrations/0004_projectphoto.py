# Generated by Django 5.1.2 on 2024-10-22 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_projects_project_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='media/project_photo', verbose_name='Фото')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.projects', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
    ]