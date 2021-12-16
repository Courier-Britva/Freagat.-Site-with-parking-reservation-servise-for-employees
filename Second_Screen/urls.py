from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('park_list', views.park_list, name='park_list'),
    path('manager', views.manager, name='manager'),
    path('worker', views.worker, name='worker'),
]
