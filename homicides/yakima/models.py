from __future__ import unicode_literals

import datetime

from django.db import models

import django_filters


class Homicide(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(blank=True)
    age = models.IntegerField()
    year = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    x = models.DecimalField(max_digits=20, decimal_places=8)
    y = models.DecimalField(max_digits=20, decimal_places=8)
    method = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    status_link = models.CharField(max_length=200, blank=True)
    story = models.CharField(max_length=400)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class HomicideFilter(django_filters.FilterSet):
    class Meta:
        model = Homicide
        fields = ['city', 'method', 'status', 'age', 'year']
