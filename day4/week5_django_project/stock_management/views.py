from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Burger
from .forms import BurgerForm


## Core Mission - show burgers as unordered list
def show_burgers(request) : #{
    burger_all = Burger.objects.all()
    return render(request, 'read_burgers.html', {'burger_list':burger_all})
#}

## Bonus Mission
def create_burger(request) : #{
    if request.method == 'POST' : #{
        form = BurgerForm(request.POST)
        if form.is_valid : #{
            form.save()
        #}
        return redirect('read_burger')
    #}

    burger_all = Burger.objects.all()
    form = BurgerForm()
    return render(request, 'create_burger.html', {'burger_list':burger_all, 'burger_form':form})
#}

@csrf_exempt
def update_burger(request, pk) : #{

    burger = get_object_or_404(Burger, pk=pk)

    if request.method == 'POST' : #{  ## Update
        form = BurgerForm(request.POST, instance=burger)
        if form.is_valid : #{
            form.save()
        #}
        return redirect('read_burger')
    #}
    elif request.method == 'DELETE' : #{  ## DELETE
        burger.delete()

        return redirect('read_burger')
    #}

    form = BurgerForm(instance=burger)
    return render(request, 'update_burger.html', {'burger_form':form})
#}

