from django.shortcuts import render

# Create your views here.
def index(request):
    myinfo = {}
    myinfo['name'] = 'YILGUK SEO'
    myinfo['major'] = 'Business Administration'
    myinfo['interest'] = 'AI'
    return render(request, 'homepage/index.html', {'myinfo':myinfo}) # Must add template dir in settings.py