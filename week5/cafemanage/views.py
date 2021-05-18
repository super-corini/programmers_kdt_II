from .models import Coffee
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .forms import CoffeeForm 

# Create your views here.
class Index(View):
    def get(self, request):
        coffee_all = Coffee.objects.all()
        form = CoffeeForm()
        return render(request, 'menu.html', {"coffee_list" : coffee_all, "coffee_form" : form})
    
    def post(self, request):
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/coffee/")
    
def put(request):
    name = request.GET["name"]
    coffee = get_object_or_404(Coffee, name = name)
    coffee.price = request.GET["price"]
    coffee.save()
    return redirect("/coffee")


def delete(request, pk):
    coffee = get_object_or_404(Coffee, name = pk)
    coffee.delete()
    return redirect("/coffee/")
