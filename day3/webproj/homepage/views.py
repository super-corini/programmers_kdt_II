from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    #return HttpResponse("Hello world!")
    return render(request,'index.html',{})