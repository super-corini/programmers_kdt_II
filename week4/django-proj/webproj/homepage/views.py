from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    nums = [1,2,3,4,5]
    return render(request, 'portfolio.html')

