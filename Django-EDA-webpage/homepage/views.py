from __future__ import unicode_literals
from django.shortcuts import HttpResponse, render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def explore_1(request):
    return render(request, 'explore_1.html')

def establish_2(request):
    return render(request, 'establish_2.html')

def test_2(request):
    return render(request, 'test_2.html')

def eda_3(request):
    return render(request, 'eda_3.html')