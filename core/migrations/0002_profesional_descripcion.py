# Generated by Django 4.2.11 on 2024-04-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesional',
            name='descripcion',
            field=models.TextField(default='', max_length=450),
        ),
    ]