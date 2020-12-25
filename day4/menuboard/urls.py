from django.urls import path
from . import views

app_name = 'menuboard'
urlpatterns = [
    path('', views.profile, name="profile"),
    path('fruits/', views.fruit_create_read, name="fruit_create_read"),
    path('fruits/<int:pk>', views.fruit_update_delete, name="fruit_update_delete"),
]