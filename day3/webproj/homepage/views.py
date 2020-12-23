from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    name = "정현호"
    age = 25
    hobby = ["컴퓨터", "자전거", "영상 시청"]
    return render(request, 'index.html', {"my_name": name, "my_age": age, "my_hobby": hobby}) # http request, response file, used index