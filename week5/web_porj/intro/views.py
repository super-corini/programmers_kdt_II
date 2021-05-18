from django.shortcuts import HttpResponse, render
from .models import Coffee

# Create your views here.
def index(request):
    name = "Baek SunHee"

    return render(request, 'index.html', {"my_name": name})

def coffee_view(request):
    coffee_all = Coffee.objects.all() # select * from Coffee;
    return render(request, 'coffee.html', {"coffee_list": coffee_all})