from django.db import models
from django.utils import timezone
from stock import models as product


class Sale(models.Model):
    # product = models.ForeignKey(product.Stock)
    date = models.DateField(default=timezone.now)
    product = models.CharField(max_length=650)
    quantity = models.IntegerField(default=0)
    unit = models.FloatField(default=0)
    unit_price = models.FloatField(default=0)
    amount = models.FloatField(default=0)

    def __str__(self):
        return self.product
