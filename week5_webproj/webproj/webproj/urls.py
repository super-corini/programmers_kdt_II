"""webproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from homepage.views import index, introduce, coffee_view, burger_view, update_delete_burger
urlpatterns = [
    path('', index), # 127.0.0.1/
    path('intro/', introduce), # 127.0.0.1/intro
    path('coffee/', coffee_view), # 127.0.0.1/coffee/
    path('burger/', burger_view, name="burgers"), # 127.0.0.1/burger/
    path('burger/<int:pk>', update_delete_burger, name="update_delete_burger"),
    path('admin/', admin.site.urls), # 127.0.0.1/admin/
]
