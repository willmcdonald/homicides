# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 01:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yakima', '0003_auto_20170131_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='homicide',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
