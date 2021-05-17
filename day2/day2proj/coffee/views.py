from django.shortcuts import HttpResponse, render
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
    return render(request, "coffee/coffee.html", context)
