# Generated by Django 2.2.19 on 2021-03-18 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0003_auto_20210318_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirect',
            name='key',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]