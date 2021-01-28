from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import logout

urlpatterns = [
    url(r'signup/$', views.signup, name= 'signup'),
    url(r'^login/$', views.loginpage, name= 'login'),
    url(r'logout/$', views.logoutuser, name= 'logout'),