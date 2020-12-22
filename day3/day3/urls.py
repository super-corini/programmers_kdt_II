"""day3 URL Configuration

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
from homepage.views import index, CoffeeView, coffee_create, coffee_update

coffee_patterns = [
    path('', CoffeeView.as_view()),
    path('create/', coffee_create),
    path('update/<int:coffee_id>', coffee_update),

]

urlpatterns = [
    path('', index),
    path('coffees/', include(coffee_patterns)),
    path('admin/', admin.site.urls),
]
