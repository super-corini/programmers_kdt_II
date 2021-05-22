from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html',{'name':'조현욱','age':26})

def secret(request):
    return render(request,'secret.html',{})