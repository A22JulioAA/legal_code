# Generated by Django 4.2.11 on 2024-04-28 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0006_alter_comentario_fecha_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha_comentario',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 28, 17, 28, 12, 979944)),
        ),
    ]