# Generated by Django 3.2 on 2021-06-21 12:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_rename_photomodels_photomodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photomodel',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]