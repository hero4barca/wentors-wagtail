# Generated by Django 3.2.10 on 2022-07-25 15:36

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0096_aboutpage_testimony_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programspage',
            name='programs_list',
            field=wagtail.core.fields.StreamField([('programs', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Program', help_text='program name')), ('description_text', wagtail.core.blocks.RichTextBlock(blank=True, help_text='provide detailed course description here')), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(default='Click')), ('link', wagtail.core.blocks.CharBlock(default='#'))])), ('program_breakdown', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('sub_title', wagtail.core.blocks.CharBlock(default='Program sub-title', help_text='sub-title')), ('text', wagtail.core.blocks.RichTextBlock(help_text='description of specified sub-title or breakdown')), ('img', wagtail.images.blocks.ImageChooserBlock(help_text='descriptive image/campaign image', required=False))]), required=False))]), min_num=1))], help_text='list various programs and provide details'),
        ),
    ]
