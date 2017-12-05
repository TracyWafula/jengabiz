from django import forms
from .models import Stock


class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ['date', 'product', 'quantity', 'unit', 'unit_price', 'amount']