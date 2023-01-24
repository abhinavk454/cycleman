from django.db import models


class Cycle(models.Model):
    """Cycle Model"""
    
    name = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
