from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Fruit
from .forms import FruitForm

# Create your views here.
def index(request):
    lst = [1,2,3,4,5]
    return render(request, 'index.html', {"my_list":lst})

def fruit(request):
    data = Fruit.objects.all()
    return render(request, 'fruit.html', {"fruit":data})

def fruit_new(request):
    if request.method == "POST":
        form = FruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fruit')
    else:
        form = FruitForm()
    return render(request, 'fruit_new.html', {"fruit_form":form})

def fruit_edit(request, pk):
    item = get_object_or_404(Fruit, pk=pk)
    if request.method == "POST":
        form = FruitForm(request.POST, instance=item)
        if form.is_valid():
            post = form.save()
            return redirect('fruit')
    else:
        form = FruitForm(instance=item)
    return render(request, 'fruit_edit.html', {"fruit_form":form})

def fruit_delete(request, pk):
    item = get_object_or_404(Fruit, pk=pk)
    item.delete()
    return redirect('fruit')
