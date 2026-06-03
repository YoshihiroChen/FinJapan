from django.urls import path
from . import views

urlpatterns = [
    path('', views.investment_home, name='investment_home'),
]