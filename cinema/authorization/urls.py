from django.urls import path

from . import views
#from ..home.views import home

urlpatterns = [
    #url(r'^$', home),
    #path('signup/
    path(r'reg_form', views.reg_form),
    path(r'log_in', views.log_in_form),
]
