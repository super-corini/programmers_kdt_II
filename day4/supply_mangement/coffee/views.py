from django.shortcuts import get_object_or_404, redirect, render
from .models import Coffee
from .forms import CoffeeForm
from django.http import HttpResponse, JsonResponse
from django.views import View
import json

# Create your views here.


class IndexView(View):
    def __init__(self, **kwargs) -> None:
        self.coffee_all = Coffee.objects.all().order_by("order_date")

    def get(self, request):

        form = CoffeeForm()
        return render(
            request,
            "coffee.html",
            {"coffee_list": self.coffee_all, "coffee_form": form},
        )

    def post(self, request):
        coffee_all = Coffee.objects.all().order_by("order_date")
        form = CoffeeForm(request.POST)
        if form.is_valid:
            form.save()
        return render(
            request, "coffee.html", {"coffee_list": coffee_all, "coffee_form": form}
        )

    def put(request, pk):
        coffee = get_object_or_404(Coffee, pk=pk)
        form = CoffeeForm(request.POST or None, instance=coffee)
        if form.is_valid():
            form.save()
            return redirect("/coffees")

        return render(
            request, "coffee_PUT.html", {"coffee_info": coffee, "coffee_form": form}
        )

    def delete(request, pk):
        coffee = Coffee.objects.all().order_by("order_date").get(pk=pk)
        coffee.delete()
        return redirect("/coffees")
