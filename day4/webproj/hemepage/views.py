from django.shortcuts import HttpResponse, render
from .models import Coffee
from .model import Coffees
from .forms import CoffeeForm
from .forms import CoffeesForm

# Create your views here.
def index(request):
    name = "Michael"
    nums = [1, 2, 3, 4, 5]
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'index.html', {"my_list": nums})   # 요청 + 보여질 파일 + {추가 데이터}: import와 비슷

def coffee_view(request):
    coffee_all = Coffee.objects.all()   # .all():Coffee의 모든 object(행)을 가져옴, .get(), .filter(), ...
    # 만약 request가 POST라면:
        # POST 바탕으로 Form을 완성하고
        # Form이 유효하면 -> 저장!
    if request.method == 'POST':
        form = CoffeeForm(request.POST) # 완성된 Form
        if form.is_valid(): # 채워진 Form이 유효하다면:
            form.save() # 이 Form 내용을 Model에 저장

    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list" : coffee_all, "coffee_form" : form})

def coffees_view(request):
    coffee_all = Coffees.objects.all()

    if request.method == 'POST':
        form = CoffeesForm(request.POST)
        if form.is_valid():
            form.save()

    form = CoffeesForm()
    return render(request, 'coffees.html', {"coffees_list" : coffee_all, "coffees_form" : form})


# PUT/DELETE

# 1. 기존 기능으로 해결
# - GET/POST로 해결 + endpoint 수정
# - POST coffee/edit

# 2. Middleware
# - log 찍기
# - HTTP Verb Hijack

# 3. DRF

# uWSGI, Nginx
# - 배포를 위한 과정