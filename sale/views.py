from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import generic
from .models import Sale
from django.shortcuts import render, redirect
from .form import UserForm, SaleForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm


class IndexView(generic.ListView):
    template_name = 'sale/sale_list.html'
    context_object_name = 'all_sale'

    def get_queryset(self):
        return Sale.objects.all()


class SaleCreate(CreateView):
    template_name = 'sale/sale_form.html'
    model = Sale
    fields = ['date', 'product', 'quantity', 'unit', 'unit_price', 'amount']


def about(request):
    return render(request, 'sale/about.html')


def home(request):
    return render(request, 'sale/index.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'sale/login_user.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'sale/index.html')
            else:
                return render(request, 'sale/login_user.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'sale/login_user.html', {'error_message': 'Invalid login'})
    return render(request, 'sale/login_user.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'sale/details.html')
    context = {
        "form": form,
    }
    return render(request, 'sale/register.html', context)














