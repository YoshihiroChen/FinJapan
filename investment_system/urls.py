from django.urls import path
from . import views

urlpatterns = [
    path("", views.guide, name="investment_system"),
    path("nisa/", views.nisa, name="investment_nisa"),
    path("ideco/", views.ideco, name="investment_ideco"),
    path("pension/", views.pension, name="investment_pension"),
]
