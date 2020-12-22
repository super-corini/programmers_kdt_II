from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'title': '강기주',
        'subTitle': '1기',
        'description': '디...장고',
        'stack': ['React', 'UWP', 'Spring'],
        'location': '서울',
        'lang': '0개 국어',
        'website': '부끄',
    })
