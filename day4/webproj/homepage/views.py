from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse, render, redirect
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'index.html',{})

def coffee_view(request):
    coffee_all = Coffee.objects.all() # .get(), .filter()
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
    form = CoffeeForm()
    return render(request, 'coffee.html',{"coffee_list":coffee_all, "coffee_form":form})

def edit_coffee(request, pk):
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            change_instance = Coffee.objects.get(name=pk)
            change_instance.delete()
            change_instance=form
            change_instance.save()
        return redirect('http://127.0.0.1:8000/coffees/')
    elif request.method == "GET":
        
        delete_instance = Coffee.objects.get(name=pk)
        delete_instance.delete()
        return redirect('http://127.0.0.1:8000/coffees/')
    else:
        return HttpResponse("ERROR")
