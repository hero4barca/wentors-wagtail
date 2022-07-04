# Generated by Django 3.2.10 on 2022-07-04 13:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0094_aboutpage_testimony_top_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='testimony_cards',
            field=wagtail.core.fields.StreamField([('testimonials', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(default='Firstname Lastname')), ('current_position', wagtail.core.blocks.CharBlock(default='Job description')), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('testimony', wagtail.core.blocks.TextBlock(default='The testimony provided by user. One paragraph only (roughly 35 words)'))])))], help_text='Testimonies from former wentees', null=True),
        ),
    ]
