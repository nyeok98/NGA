# Generated by Django 3.1 on 2020-08-13 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200813_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='blog',
            name='fees',
            field=models.IntegerField(default=1000, verbose_name='Fees'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='limited_time_hour',
            field=models.IntegerField(default=0, verbose_name='Hour'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='limited_time_min',
            field=models.IntegerField(default=0, verbose_name='Minute'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='limited_time_sec',
            field=models.IntegerField(default=0, verbose_name='Second'),
        ),
    ]
