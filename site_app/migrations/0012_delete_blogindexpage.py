# Generated by Django 3.2.10 on 2021-12-19 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailmenus', '0023_remove_use_specific'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('site_app', '0011_auto_20211218_2326'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogIndexPage',
        ),
    ]
