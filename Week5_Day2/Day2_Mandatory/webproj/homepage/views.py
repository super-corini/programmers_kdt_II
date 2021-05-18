from django.shortcuts import HttpResponse, render
from datetime import datetime
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    coffee_all = Coffee.objects.all()
    return render(request, 'index.html', {"coffee_list" : coffee_all})

def coffee_view(request):
    coffee_all = Coffee.objects.all() # .get(), .filter(), ...
    # 만약 request가 POST 라면:
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면 -> 저장!
    if request.method =="POST":
        form = CoffeeForm(request.POST) # 완성된 Form
        if form.is_valid(): # 채워진 Form이 유효하다면:
            form.save() # 이 Form 내용을 Model에 적용

    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list" : coffee_all, "coffee_form" : form})

def update(request, pk):
    coffee = get_object_or_404(Coffee, pk)
    if request.method == "PUT":
        form = CoffeeForm(request.PUT, instance = coffee)
        if form.is_valid():
            form.save()
            return redirect('coffee')
    
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list" : coffee_all, "coffee_form" : form})



    