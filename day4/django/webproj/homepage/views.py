from django.shortcuts import HttpResponse, render
from .models import coffe
# Create your views here.

def index(request):
    number=10
    return render(request,'index.html')
def coffee(request):

    coffe_all=coffe.objects.all()

    return render(request,'coffee.html',{ "coffee_list":coffe_all})


