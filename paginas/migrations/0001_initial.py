# Generated by Django 4.0.4 on 2022-06-06 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paginas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('copete', models.CharField(max_length=255)),
                ('cuerpo', models.CharField(max_length=2000)),
                ('imagen', models.CharField(max_length=50)),
                ('habilitada', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'pagina',
                'verbose_name_plural': 'paginas',
            },
        ),
    ]