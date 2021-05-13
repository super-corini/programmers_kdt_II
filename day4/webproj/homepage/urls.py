from django.urls import path
from homepage.views import index, coffee_view, coffee_modify

app_name = "homepage"

urlpatterns = [
    path('', coffee_view),
    path('<int:pk>/delete', coffee_modify),
    path('<int:pk>/put', coffee_modify),
]
