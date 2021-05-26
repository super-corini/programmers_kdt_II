from django.urls import path
from . import views

app_name = 'eda'

urlpatterns = [
    path('', views.home, name="home"),
]