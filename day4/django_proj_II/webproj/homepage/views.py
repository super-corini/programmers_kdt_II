from django.shortcuts import render, get_object_or_404, redirect
from .models import Bakery
from .forms import BakeryForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def bakery_view(request):
    bakery_all=Bakery.objects.all()#.order_by('name')

    if request.method=="POST":
        form=BakeryForm(request.POST)
        if form.is_valid():
            form.save()

    form=BakeryForm()

    return render(request, 'bakery.html', {'bakery_list':bakery_all, 'bakery_form':form})

def bakery_update(request, pk):
    bakery_=Bakery.objects.get(pk=pk)

    if request.method=="POST":
        bakery_.name=request.POST['name']
        bakery_.price=request.POST['price']
        bakery_.stock=request.POST['stock']
        bakery_.save()
        return redirect('/bakery')

    return render(request, 'update.html', {'bakery_form' : bakery_})

def bakery_delete(request, pk):
    bakery_it=Bakery.objects.get(pk=pk)
    bakery_it.delete()
    return redirect('/bakery')