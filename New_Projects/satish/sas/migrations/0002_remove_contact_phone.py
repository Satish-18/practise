# Generated by Django 3.0.6 on 2020-07-01 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]