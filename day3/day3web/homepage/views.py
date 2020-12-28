from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def kor(request):
    return render(request, 'kor.html')
    

def coffee_view(request):
    coffee_all = Coffee.objects.all()
    form       = CoffeeForm()

    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'coffee.html', 
        {"coffee_list": coffee_all, "coffee_form":form})


# 파라미터로 입력받은 id를 t에 저장합니다. 
def update_load(request):
    coffee_all = Coffee.objects.all()
    f          = CoffeeForm()

# 전역변수로 ids를 선언하고, id 변수를 가져오고 데이터베이스에서 꺼내옵니다.
    global ids
    ids  = request.GET.get('id', None)
    t    = get_object_or_404(Coffee, pk=ids)
    form = CoffeeForm(initial={'name':t.name, 'price':t.price, 'is_ice':t.is_ice})

# 꺼내진 데이터베이스를 돌려주어 웹 상에 표현합니다.
    return render(request, 'coffee.html', 
        {"coffee_list": coffee_all, "coffee_form":f, "update_form":form})


# 전역변수 ids를 활용하여 instance에 할당, 바뀐 정보를 저장합니다.
def update(request):
    t = get_object_or_404(Coffee, pk=ids)
    form = CoffeeForm(request.POST, instance=t)
    if form.is_valid():
        form.save()
    return redirect('/coffee')

# 삭제는 간단하게, GET 방식으로 지우고 redirect합니다.
def delete(request):
    id = request.GET.get('id', None)
    get_object_or_404(Coffee, pk=id).delete()

    return redirect('/coffee')