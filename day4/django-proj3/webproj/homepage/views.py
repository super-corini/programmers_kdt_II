# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def coffee_view(request):
    coffee_all = Coffee.objects.all()
    context = {'coffee_list':coffee_all}
    return render(request, 'coffee.html', context)

def detail(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    return render(request, 'detail.html', {'coffee': coffee})

def create(request):
    if request.method == 'POST':
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coffee_view')
    else:
        form = CoffeeForm()
    return render(request, 'create.html', {'form':form})

def update(request, pk):
    post = get_object_or_404(Coffee, pk=pk)

    if request.method == 'POST':
        form = CoffeeForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('coffee_view')
        
    else:
        form = CoffeeForm(instance=post)
    return render(request, 'update.html', {'form': form})

def delete(request, pk):
    coffee = Coffee.objects.get(pk=pk)
    coffee.delete()
    return redirect('coffee_view')