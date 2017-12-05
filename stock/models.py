from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Stock(models.Model):
    date = models.DateField(default=timezone.now)
    product = models.CharField(max_length=650)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=650)
    unit_price = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.product

