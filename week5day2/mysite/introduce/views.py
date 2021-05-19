from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    return render(request, 'introduce/index.html')

def coffee_view(request):
	coffee_all = Coffee.objects.all()
	if request.method == "POST":
		form = CoffeeForm(request.POST)
		if form.is_valid():
			form.save()
	form = CoffeeForm()
	return render(request, 'coffee/coffee.html', {"coffee_list" : coffee_all, "coffee_form" : form})

def coffee_remove(request):
	if request.method == 'POST':
		form = CoffeeForm()
		coffee_all = Coffee.objects.all()
		item_id = int(request.POST.get('item_id'))
		item = Coffee.objects.get(id=item_id)
		item.delete()
		return redirect('/coffee/')

def coffee_update(request):
	if request.method == 'POST':
		item_id = int(request.POST.get('item_id'))
		item = Coffee.objects.get(id=item_id)
		form = CoffeeForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
		return redirect('/coffee/')