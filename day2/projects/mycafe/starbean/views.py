from django.shortcuts import get_object_or_404, redirect, render

from .forms import CoffeeForm
from .models import Coffees


def index(request):
    info = {
        "name": "MEI Y.",
        "email": "devmei.n@gmail.com",
        "majors": ["Physics", "ICEE(Information, Communications and Electronic Engineering)"],
        "skills": ["JS", "Java", "python", "C"],
        "studying": ["Statistics and Data Science", "AI"]
    }
    return render(request, 'index.html', info)


def coffee_list(request):
    # GET /coffees
    coffees = Coffees.objects.all()
    context = {'coffee_list': coffees}
    return render(request, 'coffee.html', context)


def create_coffee(request):
    # POST /coffees
    if request.method == 'POST':
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = CoffeeForm()
    return render(request, 'form.html', {'form': form})


def update_coffee(request, coffee_id):
    # PUT /coffees/<pk>
    coffee = get_object_or_404(Coffees, pk=coffee_id)
    if request.method == 'POST':
        form = CoffeeForm(request.POST, instance=coffee)
        if form.is_valid():
            coffee = form.save(commit=False)
            coffee.save()
            return redirect('list')
    else:
        form = CoffeeForm(instance=coffee)
    return render(request, 'form.html', {'form': form})


def delete_coffee(request, coffee_id):
    # DELETE /coffees/<pk>
    coffee = get_object_or_404(Coffees, pk=coffee_id)
    coffee.delete()
    return redirect('list')
