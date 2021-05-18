from django.shortcuts import render, HttpResponse
from .models import Coffee, Burger
from .forms import CoffeForm, BurgerForm


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


def coffee_view(request):
    coffee_all = Coffee.objects.all()  # .get(), .filter(), ...
    # 만약 요청이 포스트라면:
        # 포스트를 바탕으로 폼을 완성하고
        # 폼이 유효하면 -> 저장!
    if request.method == "POST":
        form = CoffeForm(request.POST)  # 완성된 폼
        if form.is_valid():  # 채워진 폼이 유효하다면
            form.save()  # 이 폼 내용을 모델에 저장

    form = CoffeForm()
    return render(request, 'coffee.html', {"coffee_list": coffee_all, "coffee_form": form})


def burger_view(request):
    burger_all = Burger.objects.all()
    if request.method == "POST":
        form = BurgerForm(request.POST)
        if form.is_valid():
            form.save()

    form = BurgerForm()
    return render(request, 'burger.html', {"burger_list": burger_all, "burger_form": form})
