# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=300, verbose_name='Почта пользователя')),
                ('photo', models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фото пользователя',
                'verbose_name_plural': 'Фото пользователей',
            },
        ),
    ]
