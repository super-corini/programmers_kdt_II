from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Coffee, Icecream
from .forms import CoffeeForm, IcecreamForm


# Create your views here.
def index(request):
    nums = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {"my_list": nums})


def coffee_view(request):
    coffee_all = Coffee.objects.all()
    # 만약 request가 POST라면:
    if request.method == "POST":
        # POST를 바탕으로 Form을 완성하고
        form = CoffeeForm(request.POST)
        # Form이 유효하면 -> Model에 저장!
        if form.is_valid():
            form.save()

    form = CoffeeForm()
    return render(request, 'coffee.html', {'coffee_list': coffee_all, 'coffee_form': form}) 


def icecream_view(request):
    icecream_all = Icecream.objects.all()
    if request.method == "POST":
        form = IcecreamForm(request.POST)
        if form.is_valid():
            form.save()

    form = IcecreamForm()
    return render(request, 'icecream.html', {'icecream_list': icecream_all, 'icecream_form': form})


