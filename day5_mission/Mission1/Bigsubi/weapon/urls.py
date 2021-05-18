from django.urls import path
from . import views

app_name = 'weapon'
urlpatterns = [
    path('whoami/', views.IndexView.as_view(), name="index"),
    path('echo', views.Return_Str, name="echo"),
    path('weapon/', views.Weapon_admin.as_view(), name="weapon")
]
