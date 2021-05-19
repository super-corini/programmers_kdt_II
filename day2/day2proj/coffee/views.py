from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.


def coffee_view(request):
    coffee_all = Coffee.objects.all()

    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()

    form = CoffeeForm()

    context = {"coffee_list": coffee_all, "coffee_form": form}
    return render(request, "coffee/main.html", context)


def coffee_detail(request, coffee_id):
    method = request.POST.get("_method", "")
    coffee = get_object_or_404(Coffee, id=coffee_id)

    if method == "PUT":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            coffee.name = request.POST.get("name", coffee.name)
            coffee.price = request.POST.get("price", coffee.price)
            coffee.is_ice = request.POST.get("is_ice", False)
            coffee.save()

        return redirect("coffee:main")

    elif method == "DELETE":
        coffee.delete()

        return redirect("coffee:main")

    form = CoffeeForm()
    context = {"coffee": coffee, "form": form}
    return render(request, "coffee/detail.html", context)
