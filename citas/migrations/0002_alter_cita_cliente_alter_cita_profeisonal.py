# Generated by Django 4.2.11 on 2024-04-29 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profesional_campo'),
        ('citas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='profeisonal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profesional'),
        ),
    ]
