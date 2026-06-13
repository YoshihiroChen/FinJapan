from django.urls import path
from .views import investment_accounts

urlpatterns = [
    path("", investment_accounts, name="investment_accounts"),
]
