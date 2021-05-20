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
from homepage.views import index, coffee_view, coffee_edit
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index), # 127.0.0.1/
    path('admin/', admin.site.urls), # 127.0.0.1/admin/
    path('index/', index), # 127.0.0.1/index
    path('coffees/', coffee_view), # 127.0.0.1/coffees
    path('coffees/<int:pk>', coffee_edit), # 127.0.0.1/coffees/<int:pk>
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
