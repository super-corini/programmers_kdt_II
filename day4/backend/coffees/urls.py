from django.urls import path
from . import views


app_name = 'coffees'

urlpatterns = [
    path('', views.coffees, name='coffees'),
    path('<int:pk>', views.coffee_modify, name='coffee_modify')
]