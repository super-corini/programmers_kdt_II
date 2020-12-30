from django.shortcuts import render, HttpResponse
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    nums = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {"my_list" : nums})

def coffee_view(request):
    coffee_all = Coffee.objects.all()   # 커피 클래스의 모든 행을 가져오라는 뜻.
    if request.method == "POST":
        form = CoffeeForm(request.POST)    # 양식이 채워진 Form 생성
        if form.is_valid():     # is_valid는 form 내부 값들이 유효한지 확인한다
            form.save()     # Form 내용을 모델에 저장
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list" : coffee_all, "coffee_form" : form})