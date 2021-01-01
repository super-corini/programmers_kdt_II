from django.shortcuts import render, HttpResponse, redirect
from .models import Coffee, Bread
from .forms import CoffeeForm, BreadForm


# Create your views here.


def index(request):
    # return HttpResponse("Hello World!")
    return render(request, 'index.html')


def coffee_view(request):
    coffee_all = Coffee.objects.all()  # .get(), .filter(), ...
    # request가 POST -> Form을 완성.
    # Form이 유효하면 저장.\
    if request.method == "POST":
        form = CoffeeForm(request.POST)  # 완성된 Form
        if form.is_valid():  # 채워진 Form이 유효하다면
            form.save()  # Form을 Model에 저장

    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list": coffee_all, "coffee_form": form})


def bread_stock(request):
    bread_all = Bread.objects.all()
    if request.method == "POST":
        form = BreadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(bread_stock)
    else:
        form = BreadForm()
    return render(request, 'bread.html', {"bread_stock": bread_all, "bread_form": form})


def bread_edit(request, bread_id):
    bread = Bread.objects.get(pk=bread_id)
    if request.method == "POST":
        bread.name = request.POST.get('name')
        bread.count = request.POST.get('count')
        bread.save()
        return redirect(bread_stock)
    else:
        form = BreadForm()
        return render(request, 'edit.html', {"bread": bread, "bread_form": form})


def bread_delete(request, bread_id):
    bread = Bread.objects.get(pk=bread_id)
    if request.method == "POST":
        bread.delete()
        return redirect(bread_stock)


def intro(request):
    if request.method == "GET":
        return render(request, 'intro.html')
