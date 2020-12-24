from django.shortcuts import HttpResponse, render
from .models import Coffee, Chicken
from .forms import CoffeeForm, ChickenForm

# Create your views here.
def index(request):
    nums = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {"my_list" : nums})

def coffee_view(request):
    coffee_all = Coffee.objects.all()

    #만약 request가 POST라면: 
        #POST를 바탕으로 Form을 완성 
        #Form이 유효하면 -> 저장하기
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save() # Form 을 모델에 연동해 저장 
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list" : coffee_all , "coffee_form" : form})

def chicken_view(request):
    chicken_list = []
    chicken_all = Chicken.objects.all()
    return render(request, 'chicken.html', {"chicken_list" : chicken_all })
    


def intro(request):
    return render(request, 'introduce.html', {})


