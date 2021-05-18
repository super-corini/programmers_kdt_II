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
from homepage.views import index, coffee_view, introduction, BR_view
# homepage 폴더의 view.py 파일에 만든 함수들

urlpatterns = [
    path('', index), # 127.0.0.1/
    path('coffees/', coffee_view), # 127.0.0.1/coffees/
    path('BR/', BR_view), # 127.0.0.1/BR/
    path('introduction/', introduction), # 127.0.0.1/introduction/
    path('admin/', admin.site.urls),  # 127.0.0.1/admin/
]
