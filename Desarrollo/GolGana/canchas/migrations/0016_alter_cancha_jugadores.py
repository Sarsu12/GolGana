# Generated by Django 3.2.7 on 2021-09-20 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0015_alter_empresa_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='jugadores',
            field=models.CharField(choices=[(0, '5'), (1, '6'), (2, '8'), (3, '9'), (4, '10'), (5, '11')], default=0, max_length=1, verbose_name='Numero de jugadores'),
        ),
    ]
