# Generated by Django 3.2.10 on 2021-12-23 20:57

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0036_rename_crousel_slides_aboutpage_carousel_slides'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='carousel_slides',
            field=wagtail.core.fields.StreamField([('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=64)), ('text', wagtail.core.blocks.CharBlock(max_length=250)), ('slider_image', wagtail.images.blocks.ImageChooserBlock()), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(default='Click')), ('link', wagtail.core.blocks.CharBlock(default='#'))], max_num=1))]), min_num=1))], null=True),
        ),
    ]