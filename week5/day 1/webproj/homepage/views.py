from django.shortcuts import HttpResponse, render
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World!</h1>")
    nums = [1,2,3,4,5]
    return render(request,'index.html',{"my_list":nums})

def coffee_view(request):
    coffee_all = Coffee.objects.all()
    # 만약 request 가 POST라면:
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면 저장
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()

    form = CoffeeForm()
    return render(request,'coffee.html',{"coffee_list":coffee_all,"coffee_form":form})

def intro(request):
    

    return render(request,'intro.html')