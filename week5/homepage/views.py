from django.shortcuts import render

# Create your views here.
def index(request):
    #HttpResponse("Hello World")
    my_name = "Kyubum Shin"
    return render(request,'index.html',{"my_name" : my_name})