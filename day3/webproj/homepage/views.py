from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    # name = 'Michael'
    nums = [1, 2, 3, 4, 5]
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'index.html', {"my_list": nums})


def introduce(request):
    name = 'Park JungHwan'
    age = 37
    info = '인공지능 학습 하고 있습니다.'

    res = {'name': name, 'age': age, 'info': info}

    return render(request, 'introduce.html', res)
