from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Coffee

import json 
# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello world!</h1>")
    number = 50
    name = "송도훈"
    nums = [1, 2, 3, 4, 5]
    intro = [
        "name: 송도훈",
        "age: 26",
        "height: 183cm",
        "weight: 100kg",
        "job: devCourse:AI",
    ]
    """
    intro = {
        "name": "송도훈",
        "age": "26",
        "height": "183cm",
        "weight": "100kg",
        "job": "devCourse:AI",
    }
    """
    args = {
        "my_list": intro,
        "message": "name:",
        "content": name,
    }
    return render(request, "index.html", args)

def coffeeIndex(request):
    if request.method == "POST":
        req = json.loads(request.body)
        new_coffee = Coffee(
            name = req['name'],
            price = int(req['price']),
            is_ice = bool(req['is_ice']),
        )
        new_coffee.save()
        return HttpResponse("POST 요청 확인", status="200")
    elif request.method == "GET":
        coffee_all = Coffee.objects.all()
        args = {
            "coffee_list": coffee_all,
        }
        return render(request, "coffee.html", args)
    elif request.method == "PUT":
        # primary key를 name으로 지정
        # 필요시 id로 변경 후 name도 변경 가능함
        req = json.loads(request.body)
        pk = req['id']
        chg_coffee = get_object_or_404(Coffee, pk=pk)
        if 'name' in req.keys():
            chg_coffee.name = req['name']
        if 'price' in req.keys():
            chg_coffee.price = req['price']
        if 'is_ice' in req.keys():
            chg_coffee.is_ice = req['is_ice']
        chg_coffee.save()
        return HttpResponse("PUT요청 확인", status=200)
    elif request.method == "DELETE":
        req = json.loads(request.body)
        pk = req['id']
        chg_coffee = get_object_or_404(Coffee, pk=pk)
        chg_coffee.delete()
        return HttpResponse("DELETE 요청 확인", status=200)
    """
    coffee_all = Coffee.objects.all()
    args = {
        "coffee_list": coffee_all,
    }
    return render(request, "coffee.html", args)
    """