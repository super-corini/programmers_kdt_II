from django.shortcuts import render, redirect
from .models import Coffee
from .forms import CoffeeForm
# Create your views here.
def index(request):
    return render(request, 'index.html')
# 이후 migrate 작업을 진행해야 한다. 그래야 모델이 만들어진걸 알게 된다. 바로하지말고. migration 먼저 만들어.
# makemigrations -> migrate


def coffee_view(request):
    # 모든 데이터를 가져오는 대신에 get이나 filter 같은 방법을 사용 가능하다.
    coffee_all = Coffee.objects.all()
    return render(request, 'coffee.html', {"coffee_list": coffee_all})


def coffee_create(request):
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coffee')
    else:
        form = CoffeeForm()
    return render(request, 'create.html', {'coffee_form': form})


def coffee_update(request, name):
    item = Coffee.objects.get(name=name)
    if request.method == "POST":
        form = CoffeeForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('coffee')
    else:
        form = CoffeeForm()
    return render(request, 'update.html', {'coffee_form': form})


def coffee_delete(request, name):
    item = Coffee.objects.get(name=name)
    item.delete()
    return redirect('coffee')