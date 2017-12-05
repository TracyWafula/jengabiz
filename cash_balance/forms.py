from django import forms


class BalanceForm(forms.Form):
    sale = forms. FloatField()
    expense = forms.FloatField()
    balance = forms. FloatField()