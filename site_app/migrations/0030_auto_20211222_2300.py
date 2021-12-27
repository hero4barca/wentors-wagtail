# Generated by Django 3.2.10 on 2021-12-22 22:00

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0029_auto_20211222_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutpage',
            old_name='CTA_text',
            new_name='cta_text',
        ),
        migrations.RenameField(
            model_name='aboutpage',
            old_name='CTA_title',
            new_name='cta_title',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='CTA_button1_link',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='CTA_button1_text',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='CTA_button2_link',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='CTA_button2_text',
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='cta_buttons',
            field=wagtail.core.fields.StreamField([('buttons', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(default='Click')), ('link', wagtail.core.blocks.CharBlock(default='#'))]), max_num=2))], null=True),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='goals_cards',
            field=wagtail.core.fields.StreamField([('goals', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='skill')), ('text', wagtail.core.blocks.RichTextBlock()), ('img', wagtail.images.blocks.ImageChooserBlock(required=False))]), max_num=4))], null=True),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='skills_and_progress',
            field=wagtail.core.fields.StreamField([('progress', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('skill', wagtail.core.blocks.CharBlock(default='skill')), ('value', wagtail.core.blocks.IntegerBlock(default=100))]), max_num=4))], null=True),
        ),
    ]