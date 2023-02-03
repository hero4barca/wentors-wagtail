# Generated by Django 3.2.10 on 2023-02-03 14:58

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0113_alter_programspage_cohorts'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='action_button',
            field=wagtail.core.fields.StreamField([('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(default='Click')), ('link', wagtail.core.blocks.CharBlock(default='#'))]))], help_text='call to action', null=True),
        ),
    ]