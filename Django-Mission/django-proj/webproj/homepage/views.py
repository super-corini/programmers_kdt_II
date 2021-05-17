from django.shortcuts import HttpResponse, get_object_or_404, render, redirect
from .models import Coffee, CoffeeBeen
from .forms import CoffeeForm, CoffeeBeenForm

# Create your views here.
def index(request):
    nums = [1, 2, 3, 4, 5]
    name = "Michael"
    return render(request, 'index.html', {"my_name" : name, "my_list" : nums})

def introduction(request):
    name = "Dongik Jang"
    level = "Beginner"
    status = "Getting used to it"
    belong_to = "AI-B"
    return render(request, 'introduction.html', {
        "name" : name,
        "level" : level,
        "status" : status,
        "belong_to" : belong_to})

def coffee_view(request):
    coffee_all = Coffee.objects.all() # get(), filter(), ...
    # 만약 request가 POST라면:
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면 -> 저장!
    if request.method == "POST":
        form = CoffeeForm(request.POST) # 완성된 Form
        if form.is_valid(): # 채워진 Form이 유효하다면:
            form.save() # 이 Form 내용을 Model에 저장
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list" : coffee_all, "coffee_form" : form})

def coffee_stock(request):
    coffee_stock_all = CoffeeBeen.objects.all()
    return render(request, 'coffee_stock.html', {"coffee_stock_list" : coffee_stock_all})

def coffee_post(request):
    coffee_stock_all = CoffeeBeen.objects.all()
    if request.method == "POST":
        form = CoffeeBeenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/GET/coffees/')
    form = CoffeeBeenForm()
    return render(request, 'coffee_post.html', {"coffee_stock_list" : coffee_stock_all, "coffee_been_form" : form})

def coffee_put(request, pk):
    coffee_stock_get = CoffeeBeen.objects.get(name=pk)
    if request.method == "POST":
        form = CoffeeBeenForm(request.POST, instance=coffee_stock_get)
        if form.is_valid():
            form.save()
            return redirect('/GET/coffees/')
    form = CoffeeBeenForm()
    return render(request, 'coffee_put.html', {"coffee_stock_get" : coffee_stock_get, "coffee_been_form" : form})

def coffee_delete(request, pk):
    deleting_coffee = CoffeeBeen.objects.get(name=pk)
    deleting_coffee.delete()
    return redirect('/GET/coffees/')
