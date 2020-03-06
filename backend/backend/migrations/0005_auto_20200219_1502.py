# Generated by Django 3.0.3 on 2020-02-19 14:02

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200219_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=backend.models.get_image_path),
        ),
    ]