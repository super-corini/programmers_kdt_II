# 직접 만들어야함
from django.urls import path
from . import views

urlpatterns = [

	# path('<int:pk>/update/', views.post_update, name='update'),
	path('<int:pk>/delete/', views.coffee_delete, name='coffee_delete'),

]