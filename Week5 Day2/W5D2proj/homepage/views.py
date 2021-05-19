from django.shortcuts import render
from .models import Coffee

# Create your views here.
def introduce(request):
    name = "최기웅"
    age = "26"
    job = "학생"
    hobby = "영화감상"
    return render(request,'introduce.html',{"name" : name, "age" : age, "job" : job, "hobby" : hobby})


def coffees_view(request):
    if request.method == 'GET':
        coffee_all = Coffee.objects.all()
        return render(request,'coffees.html',{"coffee_list":coffee_all})
