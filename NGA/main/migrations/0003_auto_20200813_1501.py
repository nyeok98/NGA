# Generated by Django 3.1 on 2020-08-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200813_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fees',
            field=models.IntegerField(default=1000, verbose_name='number'),
        ),
    ]
