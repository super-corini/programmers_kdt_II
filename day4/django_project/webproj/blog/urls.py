# 직접 만들어야함
from django.urls import path
from . import views

urlpatterns = [

	path("", views.home, name='home'),
	path('create/', views.post_create, name='create'),
	path('<int:pk>/', views.post_detail, name='detail'),
	path('<int:pk>/update/', views.post_update, name='update'),
	path('<int:pk>/delete/', views.post_delete, name='delete'),

]