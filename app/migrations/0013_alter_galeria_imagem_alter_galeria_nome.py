# Generated by Django 5.1.5 on 2025-01-31 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_galeria_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='imagem',
            field=models.ImageField(upload_to='galerias', verbose_name='Imagem da Galeria'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome da Imagem'),
        ),
    ]
