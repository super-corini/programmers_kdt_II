from django.shortcuts import render
from .models import Bakery
from .forms import BakeryForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def bakery_view(request, pk=None):
    bakery_all=Bakery.objects.all()#.order_by('name')

    if request.method=="POST":
        form=BakeryForm(request.POST)
        if form.is_valid():
            form.save()

    form=BakeryForm()

    return render(request, 'bakery.html', {'bakery_list':bakery_all, 'bakery_form':form})