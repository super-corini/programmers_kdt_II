from django.shortcuts import HttpResponse, render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    # age = datetime.today().year - 1993 + 1
    name_kor = "이준엽"
    name_eng = "JunYup Lee"
    birth_date = "1994.03.21"
    age = datetime.today().year - 1994 + 1
    return render(request, 'about.html', {"myname_kor": name_kor, "myname_eng": name_eng, "birth_date": birth_date, "age" : age})


def interests(request):
    return render(request, 'interests.html')