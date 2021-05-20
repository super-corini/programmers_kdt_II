from django.shortcuts import render, redirect, get_object_or_404
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def coffee_view(request):
    coffee_all = Coffee.objects.all() #.get(), .filter()
    # if request is POST
    if request.method == "POST":
        form = CoffeeForm(request.POST) #완성된 Form
        if form.is_valid(): # 채워진 Form이 유효하다면
            form.save()

    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list": coffee_all,
                                           "coffee_form": form})

def coffee_ud(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    method = request.POST.get('_method', '')
    if method == "PUT":
        form = CoffeeForm(request.POST, instance=coffee)
        if form.is_valid():
            form.save()
            return redirect('coffees')
    elif method == "DELETE":
        coffee.delete()
        return redirect('coffees')
    else:
         form = CoffeeForm()
    return redirect('coffees')

