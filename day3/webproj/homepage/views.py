from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    number = 100
    nums = [1,2,3,4,5]
    name = "Bruno"
    return render(request , 'index.html', {"my_list" : nums})

def introduce(request):
    return render(request, 'introduce.html', {})