# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yakima', '0005_auto_20170201_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='homicide',
            name='image_url',
            field=models.CharField(default='http://bloximages.newyork1.vip.townnews.com/yakimaherald.com/content/tncms/assets/v3/editorial/6/44/64495a4a-bbf6-11e5-8c0a-53112e60a916/5699a6ce23d12.image.jpg', max_length=200),
            preserve_default=False,
        ),
    ]