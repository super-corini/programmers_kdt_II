from django.shortcuts import get_object_or_404, redirect, render
from .models import Coffees
from .forms import CoffeesForm

# Create your views here.
def coffees_view(request):
    coffees_list = Coffees.objects.all()
    coffees_form = CoffeesForm()

    if request.method == 'POST':
        coffees_form = CoffeesForm(request.POST)
        if coffees_form.is_valid():
            coffees_form.save()
            return redirect('coffees_view')
    # elif request.method == 'GET':
    #     return redirect('coffees_view')

    return render(request, 'coffees.html', {'coffees_list': coffees_list,
                                            'coffees_form': coffees_form})


def coffee_view(request, id):
    coffee = get_object_or_404(Coffees, id=id)
    if request.method == 'DELETE':
        coffee.delete()
        return redirect('coffees_view')

    return render(request, 'coffee.html', {'coffee': coffee})