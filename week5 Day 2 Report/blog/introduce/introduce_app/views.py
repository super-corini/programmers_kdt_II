from django.shortcuts import render, redirect
from .models import Burger
from .forms import BurgerForm

def main(request):
    return render(request, 'main.html',{})

def introduce(request):
    return render(request, 'introduce.html', {})

def like(request):
    return render(request, 'like.html', {})

def todo(request):
    return render(request, 'todo.html', {})

def burger(request):
    burger_list = Burger.objects.all()
    if request.method=='POST':
        form = BurgerForm(request.POST)
        if form.is_valid():
            form.save()
        
    form = BurgerForm()
    return render(request,'burger.html',{"burger_list":burger_list, "burger_form":form})

def ud_burger(request, burger_id):
    burger_list = Burger.objects.all()
    burger = Burger.objects.get(pk=burger_id)
    if request.method=='POST':
        if request.POST.get('name'):
            burger.name=request.POST.get('name')
            burger.price=request.POST.get('price')
            if request.POST.get('is_set')==1:
                burger.is_set=True
            else:
                burger.is_set=False
            burger.save()
            return redirect('/burger/')
        else:
            burger.delete()
            return redirect('/burger/')

    return render(request, 'ud_burger.html', {"burger_list":burger_list})
