# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-05-28 20:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appAdminAplicacion', '0003_auto_20180528_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ciudad',
            name='codigo_ciudad',
        ),
        migrations.RemoveField(
            model_name='pais',
            name='codigo_pais',
        ),
    ]
