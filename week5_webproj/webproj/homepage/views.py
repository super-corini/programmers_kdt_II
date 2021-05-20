from django import forms
import django
from django.shortcuts import HttpResponse, redirect, render, get_object_or_404
from .models import Coffee, Burger
from .forms import CoffeeForm, BurgerForm

# Create your views here.
def index(request):
    # number = 50
    name = "Hello World!!!"
    nums = [1, 2, 3, 4, 5]
    # intro_lis = ["Choi Byeongmin", "I'm Corini", "but, I'll always try to make a project"]
    return render(request, 'index.html', {"my_name": name})   # Migration을 해줄것인데 여기서 Migration은 DB적 관점이 아닌, 코드 리팩토링의 의미이다.

def introduce(request):
    
    intro_list = [
        "Byeongmin Choi",
        "Corini",
        "steady coding",
        "Developerchoi90",
    ]
    return render(request, 'introduce.html', {'intro_list': intro_list})

def coffee_view(request):
    # ...
    coffee_all = Coffee.objects.all()  # SELETE * FROM Coffee 와 같음, # .get(), filter() ...
    # 만약 request가 POST 라면:
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면 -> 저장!
    if request.method == "POST":
        form = CoffeeForm(request.POST) # 완성된 Form
        if form.is_valid(): # 채워진 Form이 유효하다면:
            form.save() # 이 Form 내용을 Model에 저장
    form = CoffeeForm()
    return render(request,'coffee.html',{'coffee_list': coffee_all, 'coffee_form': form})

def burger_view(request):
    burger_all = Burger.objects.all()
    if request.method == 'POST':
        form = BurgerForm(request.POST)
        if form.is_valid():
            form.save()
    form = BurgerForm()
    return render(request, 'burger.html', {'burger_list': burger_all, 'burger_form': form})

def update_delete_burger(request, pk):
    burger = get_object_or_404(Burger, pk=pk)
    method = request.POST.get('_method', '')
    if method == 'PUT':
        form = BurgerForm(request.POST, instance=burger)
        if form.is_valid():
            form.save()
            return redirect("burgers")
        
    elif method == "DELETE":
        burger.delete()
        return redirect("burgers")

    else:
        form = BurgerForm()
    return redirect("burgers")
