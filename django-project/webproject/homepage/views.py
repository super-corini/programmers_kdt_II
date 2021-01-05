from django.shortcuts import HttpResponse, render
from .models import Coffee, Introduction, Eda
from .forms import CoffeeForm
# render함수는 인자로 3개를 받는다
# render(request, '.html', {})
# template에서 쓸 변수는 view.py에 name처럼 선언되어있어야한다

# Create your views here.

def introduction_view(request):
    introduction_all = Introduction.objects.all() # 모두 가져온다
    return render(request, 'introduction.html', {})
# return문: 모델에서 가져온 introduction_list를 가져와서 introduction.html에 받아온다

def coffee_view(request):
    coffee_all = Coffee.objects.all() # 모두 가져온다
    # 만약 request가 POST라면
        # POST를 바탕으로 Form을 완성하고, Form이 유효하면 저장!
    if request.method == "POST":
        form = CoffeeForm(request.POST) # 완성된 Form
        if form.is_valid(): # 채워진 Form이 valid?
            form.save() # 이 Form 내용을 Model에 저장

    # 만약 request가 PUT이라면
        # POST를 바탕으로 Form을 완성하고, Form이 유효하면 저장!
    if request.method == "PUT":
        form = CoffeeForm(request.PUT) # 완성된 Form
        print(Coffee.objects.get(pk=form["name"].value()))
        if form.is_valid(): # 채워진 Form이 valid?
            pass

    # 만약 request가 DELETE라면
        # POST를 바탕으로 Form을 완성하고, Form이 유효하면 저장!
    if request.method == "DELETE":
        form = CoffeeForm(request.DELETE) # 완성된 Form
        if form.is_valid(): # 채워진 Form이 valid?

            form.save() # 이 Form 내용을 Model에 저장

    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list" : coffee_all, "coffee_form" : form})
# return문: 모델에서 가져온 coffee_list를 가져와서 coffee.html에 받아온다

def eda_view(request):
    eda_all = Eda.objects.all() # 모두 가져온다
    return render(request, 'eda.html', {})