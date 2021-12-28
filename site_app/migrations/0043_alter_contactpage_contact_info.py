# Generated by Django 3.2.10 on 2021-12-28 00:27

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0042_auto_20211228_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='contact_info',
            field=wagtail.core.fields.StreamField([('contacts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('img', wagtail.images.blocks.ImageChooserBlock(required=False))]), min_num=2))], null=True),
        ),
    ]
