# Generated by Django 3.2.10 on 2023-02-02 16:42

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0110_alter_programspage_membership_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='carousel_slides',
        ),
        migrations.RemoveField(
            model_name='programspage',
            name='programs_list',
        ),
        migrations.AlterField(
            model_name='programspage',
            name='membership_info',
            field=wagtail.core.fields.StreamField([('membership', wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.RichTextBlock(blank=True, help_text='Description of membership platform')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(default='Click')), ('link', wagtail.core.blocks.CharBlock(default='#'))])), ('features_table', wagtail.core.blocks.BooleanBlock(default=False, help_text='does this program have a comparison table to display?', required=False))]))], help_text='membership portal info', null=True),
        ),
    ]