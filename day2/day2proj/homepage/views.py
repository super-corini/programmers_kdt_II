from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    return render(request, "homepage/index.html", {})


def jarang(request):
    return render(request, "homepage/jarang.html", {})
