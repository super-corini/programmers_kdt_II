from django.shortcuts import render, HttpResponse
from .models import Coffees

# Create your views here.
def coffees(request):
    li = Coffees.objects.all()
    return render(request, "coffees/base.html", {"coffee_list":li})

def coffees_with_id(request,id):
    cf = Coffees.objects.get(id = id)
    return render(request, "coffees/index.html", {"name":cf})