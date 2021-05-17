from django.shortcuts import HttpResponse, render
import json

# Create your views here.
def index(request):
    # number = 50
    # name = "Michael"
    nums = [1, 2, 3, 4, 5]
    # intro_lis = ["Choi Byeongmin", "I'm Corini", "but, I'll always try to make a project"]
    return render(request, 'index.html', {"my_list": nums})   # Migration을 해줄것인데 여기서 Migration은 DB적 관점이 아닌, 코드 리팩토링의 의미이다.

def introduce(request):
    
    intro_list = [
        "Byeongmin Choi",
        "Corini",
        "steady coding",
        "Developerchoi90",
    ]
    return render(request, 'introduce.html', {'intro_list': intro_list})

