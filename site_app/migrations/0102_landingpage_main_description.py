# Generated by Django 3.2.10 on 2022-12-15 19:27

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0101_landingpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='main_description',
            field=wagtail.core.fields.RichTextField(default='Main description here', help_text='main description here'),
        ),
    ]
