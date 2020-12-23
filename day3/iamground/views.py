from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "my_list":[1, 2, 3]
    }
    return render(request, 'iamground/index.html', context)