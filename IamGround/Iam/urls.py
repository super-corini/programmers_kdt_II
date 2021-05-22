from django.urls import path

from . import views


urlpatterns = [
    path('companies/', views.companies, name='companies'),
    path('company/<int:pk>', views.company, name='company'),
    path('delete/<int:pk>', views.delete_company, name='delete'),
    path('modify/<int:pk>', views.modify_company, name='modify'),
]

