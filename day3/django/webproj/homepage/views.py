from django.shortcuts import HttpResponse, render

# Create your views here.

def index(request):
    number=10
    return render(request,'index.html',{"my_num":number})


