from django.shortcuts import render
from .models import Coffee

# Create your views here.
def coffee_view(request):
    coffee_all = Coffee.objects.all()
    return render(request, 'coffee.html', {'my_list' : coffee_all})
