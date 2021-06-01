from django.urls import path

from . import views


urlpatterns = [
    path('', views.main, name='eda_main'),
    path('dataset', views.dataset, name='dataset'),
    path('analysis', views.analysis, name='analysis'),
]



