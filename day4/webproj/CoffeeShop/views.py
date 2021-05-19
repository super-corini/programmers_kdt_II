from django.shortcuts import render
from .models import Coffee
# Create your views here.

def coffee_list(request):
    my_coffee_list = Coffee.objects.all()
    return render(request, 'CoffeeShop/coffee_list.html', {"my_coffee_list":my_coffee_list})