# Generated by Django 4.0.4 on 2022-04-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotas', '0003_local_alter_rota_distance_alter_rota_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rota',
            name='target',
            field=models.CharField(choices=[('A', 'Exemplo A'), ('B', 'Exemplo B'), ('C', 'Exemplo C'), ('D', 'Exemplo D'), ('E', 'Exemplo E')], max_length=1),
        ),
    ]