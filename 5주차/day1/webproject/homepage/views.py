from django.shortcuts import HttpResponse, render

# Create your views here.

def index(request):
    number = 10
    name = "raison"
    what = "인공지능 데브코스 A반"


    return render(request, 'index.html', {"my_name" : name, "what" : what})