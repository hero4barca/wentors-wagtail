# Generated by Django 3.2.10 on 2021-12-23 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0035_auto_20211223_0424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutpage',
            old_name='crousel_slides',
            new_name='carousel_slides',
        ),
    ]