from django.conf.urls import include, url
from .import views
from django.contrib.auth.views import login, logout

app_name = 'sale'

urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^sale/add/$', views.SaleCreate.as_view(), name='sale-add')



]
