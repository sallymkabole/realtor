# Generated by Django 2.1.2 on 2018-10-23 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Properties', '0003_remove_property_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='user',
        ),
    ]