# Generated by Django 5.1.2 on 2024-11-11 10:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UzAmazingTravel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carusel',
            name='id',
        ),
        migrations.AlterField(
            model_name='carusel',
            name='cl_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]