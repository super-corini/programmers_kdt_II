from __future__ import unicode_literals
from django.shortcuts import HttpResponse, render
from rest_framework import viewsets
from .serializers import CoffeeSerializer
from .models import Coffee

# Create your views here.
class CoffeeViewSet(viewsets.ModelViewSet):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

def index(request):
    # 어떤 요청이 들어왔을 때, "Hello World!"라는 response를 주는 뷰이다.
    return render(request, 'index.html',{})