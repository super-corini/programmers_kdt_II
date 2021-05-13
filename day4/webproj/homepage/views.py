from django.shortcuts import render, redirect
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    name = "Michael"
    return render(request, 'index.html', {"my_name": name})

def coffee_view(request):
    coffee_all = Coffee.objects.all()
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list": coffee_all, "coffee_form": form})

def coffee_modify(request, pk):
    if request.POST['_method'] == "DELETE":
        Coffee.objects.get(id=pk).delete()
    elif request.POST['_method'] == "PUT":
        print(request.POST)
        target = Coffee.objects.get(id=pk)
        target.name = request.POST["name"]
        target.price = int(request.POST["price"])
        try:
            request.POST["is_ice"]
            target.is_ice = True
        except:
            target.is_ice = False
        target.save()
    return redirect('/coffees')