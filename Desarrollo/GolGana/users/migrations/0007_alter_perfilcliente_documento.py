# Generated by Django 3.2.6 on 2021-09-23 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210920_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilcliente',
            name='documento',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^[0-9]{6,10}$')], verbose_name='Numero de documento'),
        ),
    ]
