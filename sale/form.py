from django import forms
from django.contrib.auth.models import User
from .models import Sale
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = ['date', 'product', 'quantity', 'unit', 'unit_price', 'amount']
