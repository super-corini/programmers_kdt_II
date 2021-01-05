"""intro URL Configuration

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
from django.conf.urls import url
from homepage.views import index, fruit, fruit_edit, fruit_new, fruit_delete
urlpatterns = [
    path('', index, name='index'), # 127.0.0.1/
    path('fruit/', fruit, name='fruit'),
    path('fruit_new/', fruit_new, name='fruit_new'),
    path('<int:pk>/fruit_edit/', fruit_edit, name='fruit_edit'),
    path('admin/', admin.site.urls),
    path('<int:pk>/fruit_delete/', fruit_delete, name ='fruit_delete'),
]
