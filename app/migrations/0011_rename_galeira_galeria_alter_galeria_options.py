# Generated by Django 5.1.5 on 2025-01-31 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_galeira_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Galeira',
            new_name='Galeria',
        ),
        migrations.AlterModelOptions(
            name='galeria',
            options={'verbose_name': 'Galeria'},
        ),
    ]
