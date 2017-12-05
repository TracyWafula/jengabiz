from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Expenses(models.Model):
    class Meta:
        verbose_name_plural = 'expenses'
    # date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=250)
    quantity = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    total_amount = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('expenses:expenses_list', kwargs={'pk': self.pk})

