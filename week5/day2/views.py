from django.shortcuts import HttpResponse, render
from .models import BaskinRobbins, Coffee
from .forms import BRForm, CoffeeForm

# Create your views here.
# 어떤 요청이 들어오면 다음 응답을 리턴  
def index(request):
    name = 'Michael'
    nums = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {'my_name':name, 'my_list':nums})

def introduction(request):
    return render(request, 'self-introduction.html', {})

def coffee_view(request):
    coffee_all = Coffee.objects.all()

    # 만약 request가 POST인 경우
    if request.method == 'POST':
        # POST를 바탕으로 Form을 완성하고
        form = CoffeeForm(request.POST)
        # Form이 유효하면 저장!
        if form.is_valid():
            form.save()
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list": coffee_all, "coffee_form":form})

def BR_view(request):
    fruits = BaskinRobbins.objects.all()

    if request.method == 'POST':
        form = BRForm(request.POST)
        if form.is_valid():
            form.save()
    form = BRForm()
    return render(request, 'BR.html', {'icecream_list':fruits, 'icecream_form': form})