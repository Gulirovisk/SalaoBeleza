# Generated by Django 5.1.5 on 2025-01-23 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_servico_horario_fim_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profissional',
            options={'verbose_name': 'Profissional', 'verbose_name_plural': 'Profissionais'},
        ),
        migrations.AlterModelOptions(
            name='servico',
            options={'verbose_name': 'Serviço', 'verbose_name_plural': 'Serviços'},
        ),
    ]
