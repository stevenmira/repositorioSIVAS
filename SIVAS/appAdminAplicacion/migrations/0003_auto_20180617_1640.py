# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-06-17 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAdminAplicacion', '0002_auto_20180617_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='hora_llegada',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='horario',
            name='hora_salida',
            field=models.TimeField(),
        ),
    ]
