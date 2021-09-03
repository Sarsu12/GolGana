# Generated by Django 3.2.6 on 2021-09-02 00:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210901_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilcliente',
            name='documento',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex='^[0-9]{9}$')], verbose_name='Numero de documento'),
        ),
    ]
