from django.urls import path

from . import views

app_name = "tax"

urlpatterns = [
    path("", views.index, name="index"),
]