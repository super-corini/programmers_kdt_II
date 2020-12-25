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
from django.urls import path, include
from homepage.views import index, Lolview


lol_patterns = [
    path('', Lolview.as_view()),
]

urlpatterns = [
    path('', index), #127.0.0.1/
    path('lol/', include(lol_patterns)),
    path('lol/<int:pk>', include(lol_patterns)), #127.0.0.1/lol
    path('admin/', admin.site.urls), #127.0.0.1/admin/
]
