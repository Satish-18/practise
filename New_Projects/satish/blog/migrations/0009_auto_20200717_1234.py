# Generated by Django 3.0.6 on 2020-07-17 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200707_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='auther',
            field=models.TextField(),
        ),
    ]