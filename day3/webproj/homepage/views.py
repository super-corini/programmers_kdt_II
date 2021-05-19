from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    myinfo = {}
    myinfo['name'] = 'YILGUK SEO'
    myinfo['major'] = 'Business Administration'
    myinfo['interest'] = 'AI'
    return render(request, 'index.html', {'myinfo':myinfo})