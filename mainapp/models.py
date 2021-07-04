
from django.db import models

PROVIDER_CHOICES = [
    ('DHL', 'DHL'),
    ('UPS', 'UPS'),
    ('TNT', 'TNT'),
]
SERVICE_CHOICES = [
    ('DHL express worldwide', 'DHL express worldwide'),
    ('DHL economy select', 'DHL economy select'),
    ('UPS express saver', 'UPS express saver'),
    ('UPS standard', 'UPS standard'),
    ('TNT express', 'TNT express'),
    ('TNT economy', 'TNT economy')
]

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=100)
    zone = models.IntegerField()
    provider = models.CharField(choices=PROVIDER_CHOICES, max_length=3)
    service = models.CharField(choices=SERVICE_CHOICES, max_length=100)


class Price(models.Model):
    zone = models.IntegerField()
    amount = models.FloatField()
    weight_category = models.FloatField()
    provider = models.CharField(choices=PROVIDER_CHOICES, max_length=3)
    service = models.CharField(choices=SERVICE_CHOICES, max_length=100)


class Surcharge(models.Model):
    amount = models.FloatField()
    provider = models.CharField(choices=PROVIDER_CHOICES, max_length=3)
    service = models.CharField(choices=SERVICE_CHOICES, max_length=100)

    
