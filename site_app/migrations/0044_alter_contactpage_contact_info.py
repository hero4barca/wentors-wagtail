# Generated by Django 3.2.10 on 2021-12-28 04:50

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0043_alter_contactpage_contact_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='contact_info',
            field=wagtail.core.fields.StreamField([('contacts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('address_or_link', wagtail.core.blocks.CharBlock()), ('handle', wagtail.core.blocks.CharBlock(required=False)), ('img', wagtail.images.blocks.ImageChooserBlock(required=False))]), min_num=2))], null=True),
        ),
    ]
