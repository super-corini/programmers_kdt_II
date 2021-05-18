from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee
from .forms import CoffeeForm
# Create your views here.
def myprofile(request):
    return render(request,'myprofile.html',{})

def coffees(request):
    coffee_all = Coffee.objects.all()
    
    if request.method == "POST":
        form1 = CoffeeForm(request.POST)
        if form1.is_valid():
            form1.save()
    
    form = CoffeeForm()
    return render(request,'coffees.html',{"coffee_list":coffee_all, "coffee_form": form})
