# Generated by Django 3.2.10 on 2021-12-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0005_auto_20211218_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpage',
            name='fifth_slide_h1',
            field=models.CharField(default='Main Text Here', max_length=50),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='fifth_slide_h2',
            field=models.CharField(default='More text here...one sentence', max_length=250),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='first_slide_h1',
            field=models.CharField(default='Main Text Here', max_length=50),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='first_slide_h2',
            field=models.CharField(default='More text here...one sentence', max_length=250),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='fourth_slide_h1',
            field=models.CharField(default='Main Text Here', max_length=50),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='fourth_slide_h2',
            field=models.CharField(default='More text here...one sentence', max_length=250),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='second_slide_h1',
            field=models.CharField(default='Main Text Here', max_length=50),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='second_slide_h2',
            field=models.CharField(default='More text here...one sentence', max_length=250),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='third_slide_h1',
            field=models.CharField(default='Main Text Here', max_length=50),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='third_slide_h2',
            field=models.CharField(default='More text here...one sentence', max_length=250),
        ),
    ]