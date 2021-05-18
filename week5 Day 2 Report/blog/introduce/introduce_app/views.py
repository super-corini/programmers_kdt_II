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

    #if request.method=='PUT':
        

    #if request.method=='DELETE':
        
    form = BurgerForm()
    return render(request,'burger.html',{"burger_list":burger_list, "burger_form":form})