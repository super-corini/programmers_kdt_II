from django.shortcuts import render
from .models import Frog

# Create your views here.
def index(request):
    return render(request,'index.html',{'name':'조현욱','age':26})

def secret(request):
    return render(request,'secret.html',{})

def frog_view(request):

    frog_all = Frog.objects.all()
    return render(request,'frog.html',{"frog_list" : frog_all})