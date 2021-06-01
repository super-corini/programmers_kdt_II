from django.urls import path
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='coffee_view'),
    path('del/<int:pk>/', IndexView.delete, name='delete_coffee'),
    path('put/<int:pk>', IndexView.put, name='update_coffee'),
    # path('post/', IndexView.post, name='post_coffee'),
]
