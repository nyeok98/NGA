# Generated by Django 3.1 on 2020-08-27 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_account_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='image',
            new_name='photo_profil',
        ),
    ]
