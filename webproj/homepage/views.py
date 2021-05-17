from django.shortcuts import HttpResponse, render
from datetime import datetime
# Create your views here.
# request에 대한 처리가 필요


def index(request):
    return render(request, 'index.html')


def intro(request):
    age = datetime.today().year - 1993 + 1
    name = "Seongwon Tak"
    return render(request, 'intro.html', {"my_age": age, "my_name": name})


def interests(request):
    return render(request, 'interests.html')
