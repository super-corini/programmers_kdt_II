from django.urls import path
from . import views


app_name = "coffee"

urlpatterns = [
    path("", views.coffee_view, name="main"),
    path("<int:coffee_id>/", views.coffee_detail, name="detail"),
]
