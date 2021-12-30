# Generated by Django 3.2.10 on 2021-12-29 23:41

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0049_maincoursepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincoursepage',
            name='courses_list',
            field=wagtail.core.fields.StreamField([('courses', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('course_name', wagtail.core.blocks.CharBlock()), ('page_link', wagtail.core.blocks.CharBlock()), ('course_type', wagtail.core.blocks.ChoiceBlock(choices=[('taught_course', 'taught_course'), ('masterclass', 'masterclass')]))])))], null=True),
        ),
        migrations.AddField(
            model_name='maincoursepage',
            name='courses_top_text',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
