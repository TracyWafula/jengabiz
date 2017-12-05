from django.views import generic
from .models import Stock
from .form import StockForm
from django.shortcuts import render,  get_object_or_404
from django.views.generic.edit import CreateView


def add_stock(request):
    if request.method == "POST":
        form = StockForm(request.POST)

        if form.is_valid():
            stock = form.save(commit=False)
            stock.save()
            return render(request, 'stock/detail.html',{'stock': stock})
    else:
        form = StockForm()
    return render(request, 'stock/create_stock.html', {'form': form})


def detail(request,stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    return render(request, 'stock/detail.html',{'stock':stock})







