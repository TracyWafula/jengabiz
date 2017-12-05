from django.conf.urls import url
from .import views

app_name = 'stock'

urlpatterns = [

    url(r'^(?P<stock_id>[0-9]+)/$', views.detail, name='detail'),
    # stock/add
    url(r'^add_stock/$', views.add_stock, name='add_stock'),



]