# Generated by Django 4.0.4 on 2022-06-13 02:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0007_alter_paginas_cuerpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paginas',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(),
        ),
    ]