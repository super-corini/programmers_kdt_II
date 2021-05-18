from django.shortcuts import render, HttpResponse
from .models import Burger

def show_burgers(request) : #{
    burger_all = Burger.objects.all()
    return render(request, 'read_burger.html', {'burger_list':burger_all})
#}
