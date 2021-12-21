# Generated by Django 3.2.10 on 2021-12-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0018_auto_20211221_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='expertise_skill_progress_bars',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='skill_1_name',
            field=models.CharField(blank=True, default='Skill 1', max_length=50),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='skill_1_progress_value',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='skill_2_name',
            field=models.CharField(blank=True, default='Skill 1', max_length=50),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='skill_2_progress_value',
            field=models.IntegerField(default=80),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='skill_3_name',
            field=models.CharField(blank=True, default='Skill 1', max_length=50),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='skill_3_progress_value',
            field=models.IntegerField(default=70),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='skill_4_name',
            field=models.CharField(blank=True, default='Skill 1', max_length=50),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='skill_4_progress_value',
            field=models.IntegerField(default=60),
        ),
    ]
