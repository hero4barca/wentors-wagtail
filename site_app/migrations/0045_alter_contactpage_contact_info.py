# Generated by Django 3.2.10 on 2021-12-28 05:06

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0044_alter_contactpage_contact_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='contact_info',
            field=wagtail.core.fields.StreamField([('contacts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('type', wagtail.core.blocks.CharBlock(choices=[('email', 'email'), ('social_media', 'social_media')], default='social_media', max_length=30)), ('address_or_link', wagtail.core.blocks.CharBlock()), ('handle', wagtail.core.blocks.CharBlock(required=False)), ('img', wagtail.images.blocks.ImageChooserBlock(required=False))]), min_num=2))], null=True),
        ),
    ]
