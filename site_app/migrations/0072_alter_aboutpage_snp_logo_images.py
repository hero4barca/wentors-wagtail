# Generated by Django 3.2.10 on 2022-02-01 14:14

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0071_auto_20220127_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='snp_logo_images',
            field=wagtail.core.fields.StreamField([('logos', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([])))], help_text='logos of partners and sponsors', null=True),
        ),
    ]
