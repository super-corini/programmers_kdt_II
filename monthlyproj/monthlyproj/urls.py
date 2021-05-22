"""monthlyproj URL Configuration

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
from edapage.views import index, intro, condition, mosthappy, comparison, koreanow
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # view 에 대한 정보 추가.
    path('', index),
    path('index', index),  # 127.0.0.1/
    path('intro', intro),
    path('condition', condition),
    path('mosthappy', mosthappy),
    path('comparison', comparison),
    path('koreanow', koreanow),
    path('admin/', admin.site.urls),  # 127.0.0.1/admin/
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)