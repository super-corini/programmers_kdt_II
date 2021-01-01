"""tutorialproj URL Configuration

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
from homepage.views import index, intro, coffee_view, bread_stock, bread_edit, bread_delete

urlpatterns = [
    path('admin/', admin.site.urls),  # 127.0.0.1/admin/
    path('', index),  # 127.0.0.1
    path('intro/', intro),  # 127.0.0.1/intro/
    path('coffee/', coffee_view),  # 127.0.0.1/coffee/
    path('breads/', bread_stock),  # 127.0.0.1/breads/
    path('breads/<int:bread_id>/', bread_edit),
    path('breads/<int:bread_id>/delete/', bread_delete)
]
