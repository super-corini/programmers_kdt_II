from django.shortcuts import render
from .models import Buger
from .forms import BugerForm


# Create your views here.
def myself(request):
    buger_all = Buger.objects.all()

    if request.method == "POST":
        form = BugerForm(request.POST)
        if form.is_valid():
            form.save()
            
    form = BugerForm
    return render(request, 'myself.html', {"buger_list" : buger_all, "buger_form": form})