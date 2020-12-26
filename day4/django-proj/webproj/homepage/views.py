from django.shortcuts import HttpResponse, render
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    # return HttpResponse("<H1>Hello World!<H1>")
    number = 10    
    name = "micheal"
    nums = [1,2,3,4,5]
    return render(request, 'index.html', {"my_num":number, "my_name":name, "my_list":nums})

def coffee_view(request):
    coffee_all = Coffee.objects.all()
    # 만약 reqeust가 POST라면:
    if request.method == "POST":
        # POST를 바탕으로 Form을 완성하고
        form = CoffeeForm(request.POST)
        # Form이 유효하면 -> 저장
        if form.is_valid():
            form.save()

    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list":coffee_all, "coffee_form":form})