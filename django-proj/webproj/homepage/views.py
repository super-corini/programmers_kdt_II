from django.shortcuts import render, HttpResponse

# Create your views here.
# 먼저 함수를 구현해야합니다.
def index(request):
    name = "Micheal"

    nums = [1,2,3,4,5]

    return render(request, 'index.html', {"my_name":name, "my_list":nums})

def me(request):
    nums = [i for i in range(1,11)]
    idx = [i+1 for i in range(1,10)]

    return render(request, 'me.html', {"game_num":nums, "idx":idx})