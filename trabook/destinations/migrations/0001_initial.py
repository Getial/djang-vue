# Generated by Django 4.2.1 on 2023-06-01 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='precio')),
                ('image_url', models.URLField(verbose_name='url de imagen')),
                ('pub_date', models.DateTimeField(verbose_name='fechaDePublicacion')),
                ('content', models.TextField(verbose_name='contenido')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='lugar')),
                ('country', models.CharField(max_length=20, verbose_name='pais')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('score', models.FloatField(verbose_name='puntuacion')),
                ('price', models.IntegerField(verbose_name='precio')),
                ('isOnDiscount', models.BooleanField(default=False, verbose_name='descuento')),
                ('priceWithDiscount', models.IntegerField(blank=True, null=True, verbose_name='precioConDescuento')),
            ],
            options={
                'verbose_name': 'Destination',
                'verbose_name_plural': 'Destinations',
                'ordering': ['place'],
            },
        ),
        migrations.CreateModel(
            name='VacationPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='lugar')),
                ('duration', models.CharField(max_length=20, verbose_name='duracion')),
                ('description', models.TextField(verbose_name='descripcion')),
                ('score', models.FloatField(verbose_name='puntuacion')),
                ('price', models.IntegerField(verbose_name='precio')),
            ],
            options={
                'verbose_name': 'VacationPlan',
                'verbose_name_plural': 'VacationPlans',
                'ordering': ['place'],
            },
        ),
    ]
