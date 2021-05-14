from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
# coffees/
# GET, POST
def index(request):
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
    coffee_all = Coffee.objects.all()
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list": coffee_all, "coffee_form": form})

# coffees/<pk>
# GET, POST(PUT), DELETE
# https://stackoverflow.com/questions/36455189/put-and-delete-django
def detail(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    method = request.POST.get('method', '').upper()
    if method == "PUT":
        form = CoffeeForm(request.POST, instance=coffee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/coffees/")
    if method == "DELETE":
        coffee.delete()
        return HttpResponseRedirect("/coffees/")
    form = CoffeeForm()
    return render(request, 'coffee_detail.html', {"coffee": coffee, "coffee_form": form})
