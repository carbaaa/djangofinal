# Generated by Django 4.0.4 on 2022-06-12 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0005_alter_paginas_copete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paginas',
            name='cuerpo',
            field=models.TextField(max_length=2000),
        ),
    ]
