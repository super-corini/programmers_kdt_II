from django.shortcuts import render
from .models import Buger


# Create your views here.
def myself(request):
    buger_all = Buger.objects.all()

    return render(request, 'myself.html', {"buger_list" : buger_all})