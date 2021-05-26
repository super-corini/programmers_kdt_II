from django.urls import path
from . import views


app_name = 'introduce'

urlpatterns = [
    path('', views.home, name='home')
]