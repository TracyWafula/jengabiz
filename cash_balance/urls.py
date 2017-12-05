from django.conf.urls import url
from cash_balance.views import BalanceView
from . import views

urlpatterns = [
    url(r'^$', BalanceView.as_view(), name='balance'),

]