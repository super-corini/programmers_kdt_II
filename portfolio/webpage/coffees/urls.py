from django.urls import path
from . import views

urlpatterns = [
    path('', views.coffees, name="coffee_view"),
    path('<int:id>', views.coffees_with_id, name="coffee_view_with_id"),
]
