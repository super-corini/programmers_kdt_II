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

# 현재 urls.py에는 /homepage/views.py에 대한 정보가 없다.
# 따라서 우리는 이 파일에 정보를 불러오기 위해 import하여 사용
from mission_1.views import myself


# path는 두 가지 인자가 필요 (경로, 그에 해당하는 것)
urlpatterns = [
    path('', myself),
    path('admin/', admin.site.urls),  # 127.0.0.1/admin
]
