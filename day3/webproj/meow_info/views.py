from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt)
def info(request):
    if request.method == 'GET':
        birth = "2013/04/13"
        name = "야옹이/meow"
        speciality_list = ["'야옹아 오빠 깨워라'고 하면 방에와서 야옹거리다가 가기",
                           "도어락 소리가 나면 문앞까지 마중나오기",
                           "'코코하자'고하면 두발로 일어서서 코로 인사하기",
                           "아빠 껌딱지 - 아빠만 보면 온갖애교 부리기"]
        return render(request, 'info.html', {"cat_birth": birth,
                                             "cat_name": name,
                                             "spaciality": speciality_list})
    else:
        return HttpResponse('<h1>Please "GET" the page!</h1>')
