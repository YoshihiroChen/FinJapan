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
    path('assets/<slug:category_slug>/', views.category, name='category'),
    path(
        'assets/<slug:category_slug>/<slug:asset_slug>/',
        views.asset_detail,
        name='asset_detail',
    ),
]
