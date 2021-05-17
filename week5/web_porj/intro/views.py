from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    name = "Baek SunHee"

    return render(request, 'index.html', {"my_name": name})
