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

from django.urls import path
from .views import index, coffee_view, phone_view, phone_pk_view

app_name = 'homepage'
urlpatterns = [
    path('', index, name='index'),  # 127.0.0.1
    path('coffee/', coffee_view, name='coffee'),  # 127.0.0.1/coffee
    path('phone/', phone_view, name='phone'),  # 127.0.0.1/phone
    path('phone/<int:pk>', phone_pk_view, name='phone'),  # 127.0.0.1/phone/<pk>
]