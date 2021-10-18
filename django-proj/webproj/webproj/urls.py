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
from homepage.views import index, coffee_view, introduce_view # type: ignore
from homepage.views import burger_view, create, update,delete # type: ignore
 # homepage 폴더에 view.py 를 불러오는 것


urlpatterns = [
    path('', index), # 127.0.0.1/ 이 주어졌을 때 해야하는 행동
    path('admin/', admin.site.urls), # 127.0.0.1/admin/ 이 주어졌을 때 하는 행동
    path('coffee/', coffee_view), # 127.0.0.1/coffee/
    path('introduce/', introduce_view),
    path('burger/', burger_view, name="main"),
    path('burger/create/', create, name='create'),
    path('burger/update/<int:pk>/',update, name='update'),
    path('burger/delete/<int:pk>/', delete, name='delete'),
]
