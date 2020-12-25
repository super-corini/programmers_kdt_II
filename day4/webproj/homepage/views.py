from django.shortcuts import render, HttpResponse, redirect
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    name = "JungEon"
    nums = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {"my_name":name, "my_list":nums})

def coffee_view(request, id=0):
    coffee_all = Coffee.objects.all()
    
    if request.method == 'PUT' or request.POST.get('_method','').upper() == 'PUT':
        menu = Coffee.objects.get(id=id)
        form = CoffeeForm(request.POST)
        if form.is_valid():
            menu.name = form.cleaned_data['name']
            menu.price = form.cleaned_data['price']
            menu.is_ice = form.cleaned_data['is_ice']
            menu.save()
        return redirect('/coffees')
        

    elif request.method == 'DELETE' or request.POST.get('_method','').upper() == 'DELETE':
        Coffee.objects.get(id=id).delete()
        return redirect('/coffees')

    elif request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/coffees')

    form = CoffeeForm()
    return render (request, 'coffee.html', {"coffee_list": coffee_all, "coffee_form": form})

