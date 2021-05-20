from django.shortcuts import render, redirect, get_object_or_404
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def coffees(request):
    if request.method == "GET":
        coffees = Coffee.objects.all()
        form = CoffeeForm()
        context = {
            'coffees': coffees,
            'form': form
        }
        return render(request, 'coffees/coffees.html', context)
    elif request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coffees:coffees')

def coffee_modify(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    if request.method == "PUT":
        form = CoffeeForm(request.PUT, instance=coffee)
        if form.is_valid():
            form.save()
            return redirect('coffees:coffees')

    elif request.method == 'DELETE':
        coffee.delete()
        return redirect('coffees:coffees')
    else:
        form = CoffeeForm(instance=coffee)
    context = {
        'form': form,
        'coffee': coffee
    }
    return render(request, 'coffees/coffee_form.html', context)