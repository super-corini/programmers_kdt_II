from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from .models import Coffee
from .models import Burger
from .forms import CoffeeForm
from .forms import BurgerForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt 
import json
from django.core.serializers import serialize


# Create your views here.
def about(request):
    return render(request, 'about.html', {})


def index(request):
    num = 17
    name = 'illstandtall'
    arr = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {"my_num": num, "my_name": name, "my_list": arr})


def coffee_view(request):
    coffee_all = Coffee.objects.all()
    # 만약 request가 POST라면:
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면 저장!
    if request.method == "POST"    :
        form = CoffeeForm(request.POST) # 완성된 Form
        if form.is_valid(): # 채워진 Form의 값들이 유효하다면:
            form.save() # 이 Form 내용을 Model에 저장 | forms.py에 Meta에 정의해두었기 때문에 가능하다.
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list": coffee_all, "coffee_form": form})


def burgers_view_unorded(request):
    burger_all = Burger.objects.all()

    if request.method == "POST"    :
        form = BurgerForm(request.POST) 
        if form.is_valid():
            form.save()
    form = BurgerForm()
    return render(request, 'burger.html', {"burger_list": burger_all, "burger_form": form})


@csrf_exempt
def burgers_post_delete(request, pk):
    try: 
        burger = Burger.objects.get(pk=pk) 
    except burger.DoesNotExist: 
        return get_object_or_404(Burger, pk=pk)
    
    if request.method == 'PUT':
        if Burger.objects.get(pk=pk):
            data = json.loads(request.body)
            burger.name, burger.price = data['name'], data['price']
            burger.save()
            return redirect(burgers_view_unorded)

    elif request.method == 'DELETE':
        burger.delete()
        return redirect(burgers_view_unorded)