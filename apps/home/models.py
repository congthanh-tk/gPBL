# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'car'