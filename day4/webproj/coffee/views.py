from django.shortcuts import render
from .models import Coffee

# Create your views here.
def index(request):
    coffee_all = Coffee.objects.all()
    return render(request, 'coffee.html', {"coffee_list":coffee_all})