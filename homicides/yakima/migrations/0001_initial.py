# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homicide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('x', models.DecimalField(decimal_places=6, max_digits=9)),
                ('y', models.DecimalField(decimal_places=6, max_digits=9)),
                ('method', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('status_link', models.CharField(max_length=200)),
            ],
        ),
    ]