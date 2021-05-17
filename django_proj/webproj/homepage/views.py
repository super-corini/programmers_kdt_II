from django.shortcuts import render

# Create your views here.
def index(request):
    nums = [1, 2, 3, 4, 5]
    # render(request, '.html'파일, {}인자들 )
    return render(request, 'index.html', {"my_list":nums})
