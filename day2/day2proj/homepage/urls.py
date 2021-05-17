from django.urls import path
from . import views


app_name = "homepage"

urlpatterns = [
    path("", views.index, name="index"),
    path("jarang/", views.jarang, name="jarang"),
]

