from django.conf.urls import url
from django.shortcuts import redirect, render
from .models import Coffee
from .forms import CoffeeForm


def index(request):
    return render(request, "index.html", {})


def coffee_view(request):
    coffee_list = Coffee.objects.all()
    if request.method == "POST":
        coffee_form = CoffeeForm(request.POST)
        if coffee_form.is_valid():
            coffee_form.save()
    coffee_form = CoffeeForm()

    return render(
        request, "coffee.html", {"coffee_list": coffee_list, "form": coffee_form}
    )


def coffee_update(request, pk):
    selected = Coffee.objects.get(pk=pk)
    form = CoffeeForm(instance=selected)
    if request.method == "POST":
        coffee_form = CoffeeForm(request.POST, instance=selected)
        if coffee_form.is_valid():
            coffee_form.save()
            return redirect("/coffee")
    return render(request, "coffee_update.html", {"form": form})


def coffee_delete(request, pk):
    selected = Coffee.objects.get(pk=pk)
    selected.delete()
    return redirect("/coffee")
