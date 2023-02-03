# Generated by Django 3.2.10 on 2023-02-03 14:36

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0112_landingpage_sponsors_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programspage',
            name='cohorts',
            field=wagtail.core.fields.StreamField([('cohorts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('cohorts_description', wagtail.core.blocks.RichTextBlock(blank=True, help_text='Description for cohorts')), ('cohorts_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(default='Click')), ('link', wagtail.core.blocks.CharBlock(default='#'))])), ('cohorts_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='cohort name', help_text='sub-title')), ('text', wagtail.core.blocks.RichTextBlock(help_text='description'))]), required=False))]), max_num=1, min_num=1))], help_text='cohorts description and details', null=True),
        ),
    ]