from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello world!")
    data = {
        'sub_page_name':'home',
        'profile': {
            '이름': '[2기-B]오준석',
            '나이': '비밀',
            '출몰지': '서울 어딘가',
            '코딩실력': 'SUPER-CORINI'
        }
    }
    return render(request, 'index.html', data)