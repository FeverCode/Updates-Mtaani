# Generated by Django 3.2 on 2022-06-19 12:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/fevercode/image/upload/v1655640806/tim-mossholder-H6eaxcGNQbU-unsplash_aq5n8o.jpg', max_length=255, verbose_name='image'),
        ),
    ]
