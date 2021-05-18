from django.urls import path
from . import views


app_name = 'cafemanage'
urlpatterns = [
    path("", views.Index.as_view(), name = "coffee"),
    path("put/", views.put, name = "putcoffee"),
    path("<str:pk>/", views.delete, name = "delcoffee"),
]
