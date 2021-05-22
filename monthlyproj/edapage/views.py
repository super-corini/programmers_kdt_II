from django.shortcuts import HttpResponse, render
# Create your views here.
# request에 대한 처리가 필요


def index(request):
    return render(request, 'index.html')

def intro(request):
    return render(request, 'intro.html')

def condition(request):
    return render(request, 'condition.html')

def mosthappy(request):
    return render(request, 'mosthappy.html')

def comparison(request):
    return render(request, 'comparison.html')

def koreanow(request):
    return render(request, 'koreanow.html')
