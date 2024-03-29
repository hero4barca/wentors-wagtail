# Generated by Django 3.2.10 on 2021-12-30 02:18

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0054_coursedetailpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetailpage',
            name='about_facilitator',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, null=True),
        ),
    ]
