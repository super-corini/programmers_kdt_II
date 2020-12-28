from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    number = 100
    nums = [1,2,3,4,5]
    return render(request , 'index.html', {"my_list" : nums})

def introduce(request):
    return render(request, 'introduce.html', {})

def coffee_view(request):
    coffee_all = Coffee.objects.all()
    # 만약 request가 POST라면:
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면, -> 저장한다
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list" : coffee_all, "coffee_form": form})

def coffee_view_detail(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    if request.method == "POST":
        form = CoffeeForm(request.POST, instance=coffee)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CoffeeForm(instance=coffee)
    return render(request, 'coffeedetail.html', {'coffee_form' : form, "coffee" : coffee})

def coffee_delete(request, pk):
    coffee = Coffee.objects.get(pk = pk)
    coffee.delete()
    return redirect('home')