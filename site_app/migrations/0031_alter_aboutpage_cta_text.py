# Generated by Django 3.2.10 on 2021-12-22 22:07

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0030_auto_20211222_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='cta_text',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
