# Generated by Django 4.2.11 on 2024-05-03 09:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_alter_comentario_fecha_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha_comentario',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
