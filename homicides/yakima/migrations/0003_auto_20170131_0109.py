# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yakima', '0002_auto_20170131_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homicide',
            name='x',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='homicide',
            name='y',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
    ]
