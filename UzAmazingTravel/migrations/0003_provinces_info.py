# Generated by Django 5.1.2 on 2024-11-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UzAmazingTravel', '0002_remove_carusel_id_alter_carusel_cl_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='provinces',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
