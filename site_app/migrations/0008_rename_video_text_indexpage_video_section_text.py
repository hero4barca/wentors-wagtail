# Generated by Django 3.2.10 on 2021-12-18 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0007_indexpage_video_section_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexpage',
            old_name='video_text',
            new_name='video_section_text',
        ),
    ]
