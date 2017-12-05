from django import forms
from .models import Expenses


class ExpensesForm(forms.ModelForm):

    class Meta:
        model = Expenses
        fields = ['name','quantity','unit_price', 'amount']
