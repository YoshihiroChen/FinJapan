from django.urls import path
from . import views

app_name = "investment"

urlpatterns = [
    path('', views.index, name='index'),

    path('cash/', views.cash, name='cash'),
    path('etf/', views.etf, name='etf'),
    path('reit/', views.reit, name='reit'),
    path('stocks/', views.stocks, name='stocks'),
    path('crypto/', views.crypto, name='crypto'),
]