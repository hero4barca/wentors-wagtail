# Generated by Django 3.2.10 on 2021-12-23 03:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0034_aboutpage_crousel_slides'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='fifth_slide',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='fifth_slide_button_link',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='fifth_slide_button_text',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='fifth_slide_h1',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='fifth_slide_h2',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='fifth_slide_img',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='first_slide_button_link',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='first_slide_button_text',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='first_slide_h1',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='first_slide_h2',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='first_slide_img',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='fourth_slide',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='fourth_slide_button_link',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='fourth_slide_button_text',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='fourth_slide_h1',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='fourth_slide_h2',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='fourth_slide_img',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='second_slide_button_link',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='second_slide_button_text',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='second_slide_h1',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='second_slide_h2',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='second_slide_img',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='third_slide',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='third_slide_button_link',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='third_slide_button_text',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='third_slide_h1',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='third_slide_h2',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='third_slide_img',
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='crousel_slides',
            field=wagtail.core.fields.StreamField([('slides', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=64)), ('text', wagtail.core.blocks.CharBlock(max_length=250)), ('slider_image', wagtail.images.blocks.ImageChooserBlock()), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(default='Click')), ('link', wagtail.core.blocks.CharBlock(default='#'))], max_num=1))]), min_num=1))], null=True),
        ),
    ]
