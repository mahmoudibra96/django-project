# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Poll (models.Model):
    text = models.CharField(max_length=300)
    pup_date=models.DateField()


    
    def __str__(self):
        return self.text



class Kaya (models.Model):
    name= models.CharField(max_length=60)


class Person (models.Model):
    name = models.CharField(max_length=60)
