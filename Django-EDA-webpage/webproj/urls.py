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
from homepage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore_1/', views.explore_1, name='explore_1'),
    path('establish_2/', views.establish_2, name='establish_2'),
    path('test_2/', views.test_2, name='test_2'),
    path('eda_3/', views.eda_3, name='eda_3'),
    path('admin/', admin.site.urls),
]
