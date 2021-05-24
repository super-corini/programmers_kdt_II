from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('coffees/', views.coffee_list, name='list'),
    path('create/', views.create_coffee, name='create'),
    path('update/<int:coffee_id>', views.update_coffee, name='update'),
    path('delete/<int:coffee_id>', views.delete_coffee, name='delete'),
]
