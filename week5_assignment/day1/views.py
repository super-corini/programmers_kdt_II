from django.shortcuts import HttpResponse, render
from .models import Burger
from .forms import BurgerForm

# Create your views here.
def introduction(request):
    name = "Ohjongseo"
    birth = "1990/12/05"
    return render(request, 'introduction.html', {"my_birth":birth, "my_name":name})

def burger_view(request):
    burger_all = Burger.objects.all()
    if request.method == 'POST':
        form = BurgerForm(request.POST)
        if form.is_valid():
            form.save()
    form = BurgerForm()
    return render(request, 'burger.html', {"burger_list":burger_all, "burger_form":form})
