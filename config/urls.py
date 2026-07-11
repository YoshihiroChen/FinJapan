"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("homepage.urls")),
    path("tax/", include("tax.urls")),
    path("investment-system/", include("investment_system.urls")),
    path("investment/", include("investment.urls")),
    path(
        "securities-bank/",
        include("securities_bank.urls")
    ),
]
