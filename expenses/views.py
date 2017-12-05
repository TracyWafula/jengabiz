from django.views import generic
from .models import Expenses
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Sum


class IndexView(generic.ListView):
    template_name = 'expenses/expenses_list'
    context_object_name = 'all_expenses'

    def get_queryset(self):
        return Expenses.objects.all()


total_amount = Expenses.objects.all().annotate(total=Sum('amount'))


class ExpensesCreate(CreateView):
    model = Expenses
    fields = ['name', 'quantity', 'unit_price', 'amount']