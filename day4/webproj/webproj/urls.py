"""webproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage.views import index, introduce, coffee_view, coffee_view_detail, coffee_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', introduce, name = 'index'),
    path('coffees/', coffee_view, name = 'home'),
    path('coffees/<int:pk>/', coffee_view_detail, name = 'detail'),
    path('coffees/<int:pk>/delete/', coffee_delete, name = 'delete')
]
