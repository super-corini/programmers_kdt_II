from django.shortcuts import render, HttpResponse
from .models import Coffees
from .forms import CoffeeForm

# Create your views here.
def index(request):
    name = "정현호"
    age = 25
    hobby = ["컴퓨터", "자전거", "영상 시청"]
    return render(request, 'index.html', {"my_name": name, "my_age": age, "my_hobby": hobby}) # http request, response file, used index


def coffe_view(request):
    coffee_all = Coffees.objects.all() # SELECT * FROM TABLE, .get(), .filter()
    # 만약 request가 POST라면:
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면 -> 저장
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save() # 이 Form 내용을 Model에 저장

    form = CoffeeForm()
    return render(request, 'coffee.html', { "coffee_list": coffee_all, "coffee_form": form})

