# Generated by Django 4.2.11 on 2024-04-29 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0007_alter_comentario_fecha_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha_comentario',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 8, 7, 20, 150760)),
        ),
    ]
