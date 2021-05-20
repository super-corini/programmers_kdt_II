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
from homepage.views import index
from CoffeeShop.views import all_coffee_list, coffee_form, coffee_PD
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index), #localhost/
    path('admin/', admin.site.urls), #localhost/admin
    path('all/', all_coffee_list, name='all'), #localhost/all-coffee : shows all coffee list
    path('coffees/', coffee_form, name='coffees-form'), #localhost/coffees
    path('coffees/<int:coffee_id>/',coffee_PD, name='coffee_PD'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)