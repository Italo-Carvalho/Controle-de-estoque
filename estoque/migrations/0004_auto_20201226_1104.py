# Generated by Django 3.1.4 on 2020-12-26 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_auto_20201226_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='birthdate',
            new_name='validade',
        ),
    ]
