# Generated by Django 3.2.7 on 2021-09-20 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0013_auto_20210920_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='jugadores',
            field=models.IntegerField(choices=[(0, '5'), (1, '6'), (2, '8'), (3, '9'), (4, '10'), (5, '11')], default=0, verbose_name='Numero de jugadores'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='image',
            field=models.ImageField(default='canchas/image/default-image.png', upload_to='media/canchas/image', verbose_name='Imagen'),
        ),
    ]
