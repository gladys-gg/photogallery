# Generated by Django 4.0.4 on 2022-05-29 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_rename_photo_photo_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='photo_category',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='photo_location',
            new_name='location',
        ),
    ]
