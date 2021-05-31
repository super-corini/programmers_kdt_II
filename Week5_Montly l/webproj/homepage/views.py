from django.shortcuts import HttpResponse, render, redirect
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def eda(request):
    return render(request, 'eda.html',{})