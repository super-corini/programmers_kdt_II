from django.urls import path
from . import views

app_name = 'geoweather'
urlpatterns = [
    path("", views.Index.as_view(), name="weather")
]