# Generated by Django 4.0.4 on 2022-05-02 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rotas', '0004_alter_rota_target'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='local',
            options={'verbose_name': 'Local', 'verbose_name_plural': 'Locais'},
        ),
        migrations.AlterModelOptions(
            name='rota',
            options={'verbose_name': 'Rota', 'verbose_name_plural': 'Rotas'},
        ),
    ]
