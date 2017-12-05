from django.db import models


class Balance(models.Model):
    class Meta:
        verbose_name_plural = 'balance'
    sale = models.FloatField(default=0)
    expense = models.FloatField(default=0)
    balance = models.FloatField(default=0)

