from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello 야옹!</h1>')
    # render(request, '.html', {})
    birth = "2013/04/13"
    name = "야옹이/meow"
    return render(request, 'index.html', {"cat_birth": birth, "cat_name": name})
