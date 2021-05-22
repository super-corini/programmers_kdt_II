from django.shortcuts import HttpResponse, render
from datetime import datetime
from .models import Coffee
from .forms import CoffeeForm


def coffee_view(request):
    coffee_all = Coffee.objects.all() # select * from coffee
    # 만약 request가 POST라면:   
    if request.method == 'POST':
        # POST를 바탕으로 form을 완성
        form = CoffeeForm(request.POST) # 완성된 Form
        # Form이 유효하면 저장하기
        if form.is_valid():
            form.save()

    form = CoffeeForm() # 빈 Form
    return render(request, 'coffee.html', {"coffee_list": coffee_all, "coffee_form":form})



def home(request):
    return render(request, 'home.html', {})


def about(request):
    my_info = {
        "name": "이수진",
        "age": datetime.now().year - 1995 + 1,
        "email": "dltnwls9623@gmail.com",
        "github": "https://github.com/dltnwls9623",
        "blog": "https://velog.io/@pengu",
        "skills": ['Python', 'JAVA', 'C', 'Keras', 'Tensorflow'],
        "research": ['Computer Vision', 'Deep Learning', 'Video Captioning'],
        "education": ['[2014.03 ~ 2017.08] 경기대학교 컴퓨터과학과','[2017.09 ~ 2019.08] 경기대학교 일반대학원']
    }
    return render(request, 'about.html', my_info)


def project(request):
    
    return render(request, 'project.html', {})


def interests(request):
    
    return render(request, 'interests.html', {})


