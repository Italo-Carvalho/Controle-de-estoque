# Generated by Django 3.1.4 on 2020-12-26 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='codigo_produto',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='country',
            new_name='codigo_produto',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='country',
            new_name='codigo_produto',
        ),
    ]
