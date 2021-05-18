from django.shortcuts import HttpResponse, render
from .models import Coffee, Fruit
from .forms import CoffeeForm, FruitForm

# Create your views here.
def index(request):
    name = "Baek SunHee"

    return render(request, 'index.html', {"my_name": name})

def coffee_view(request):
    coffee_all = Coffee.objects.all() # select * from Coffee;
    
    if request.method == "POST":
        form = CoffeeForm(request.POST) # POST를 바탕으로 Form을 완성
        if form.is_valid():
            form.save()                 # Form이 유효하면 -> 저장

    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list": coffee_all, "coffee_form":form})

def fruit_view(request):
    fruit_all = Fruit.objects.all()

    if request.method == "POST":
        form = FruitForm(request.POST)
        if form.is_valid():
            form.save()

    form = FruitForm()
    return render(request, 'fruit.html', {"fruit_list": fruit_all, "fruit_form": form})