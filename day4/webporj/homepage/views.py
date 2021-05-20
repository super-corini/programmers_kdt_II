from django.shortcuts import render
from .models import Burger

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def burger(request):
    burger_all = Burger.objects.all()
    print(burger_all)
    return render(request, 'burger.html', {'burger_list':burger_all})