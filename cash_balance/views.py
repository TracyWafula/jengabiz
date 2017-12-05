from django.shortcuts import render
from django.views.generic import TemplateView
from cash_balance.forms import BalanceForm
from django.http import HttpResponse


class BalanceView(TemplateView):
    template_name = 'cash_balance/details.html'

    def get(self, request):
        form = BalanceForm()
        return render(request, self.template_name, { 'form':form })



