from django.conf.urls import url
from .import views

app_name = 'expenses'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    # expenses/add
    url(r'^expenses/add/$', views.ExpensesCreate.as_view(), name='expenses-add'),
]