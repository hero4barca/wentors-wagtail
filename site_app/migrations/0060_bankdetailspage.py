# Generated by Django 3.2.10 on 2022-01-02 14:21

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('site_app', '0059_blogmainpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetailsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('bank_details_text', wagtail.core.fields.RichTextField(default='Wentors bank account details here')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
