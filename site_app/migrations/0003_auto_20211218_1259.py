# Generated by Django 3.2.10 on 2021-12-18 11:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('site_app', '0002_indexpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='first_slide_button_link',
            field=models.CharField(default=" ", max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpage',
            name='first_slide_button_text',
            field=models.CharField(default=" ", max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpage',
            name='first_slide_h1',
            field=models.CharField(default=" " , max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpage',
            name='first_slide_h2',
            field=models.CharField(default= " " , max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpage',
            name='first_slide_img',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='second_slide_button_link',
            field=models.CharField(default=" " , max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpage',
            name='second_slide_button_text',
            field=models.CharField(default=" ", max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpage',
            name='second_slide_h1',
            field=models.CharField(default=" " , max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpage',
            name='second_slide_h2',
            field=models.CharField(default=" ", max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpage',
            name='second_slide_img',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
