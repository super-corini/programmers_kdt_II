from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    name = "JungEon"
    nums = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {"my_name":name, "my_list":nums})