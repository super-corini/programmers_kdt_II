from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'index.html',{})