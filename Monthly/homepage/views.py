from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    history = ["data analyst","senior data scientiest"]
    return render(request, 'index.html', {'my_list':history})