# Generated by Django 4.2.1 on 2023-06-01 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0005_alter_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image_url',
            field=models.CharField(max_length=200, verbose_name='imagen'),
        ),
    ]
