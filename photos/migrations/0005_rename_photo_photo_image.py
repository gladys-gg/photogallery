# Generated by Django 4.0.4 on 2022-05-29 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photo',
            new_name='image',
        ),
    ]
