from django.urls import path
from . import views

app_name = 'menuboard'
urlpatterns = [
    path('', views.profile, name="profile"),
    path('fruits/', views.fruit_create_read, name="fruit_create_read"),
    path('fruits/<int:pk>/update/', views.fruit_update, name="fruit_update"),
    path('fruits/<int:pk>/delete/', views.fruit_delete, name="fruit_delete"),
]