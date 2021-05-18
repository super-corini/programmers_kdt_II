from django.shortcuts import HttpResponse, render, redirect ,get_object_or_404
from .models import coffe
# Create your views here.
from .forms import coffeForm


def index(request):
    number=10
    return render(request,'index.html')
def coffee(request):

    if request.method=='POST':
        form = coffeForm(request.POST)
        if form.is_valid():
            form.save()

    form=coffeForm()
    coffe_all=coffe.objects.all()

    return render(request,'coffee.html',{ "coffee_list":coffe_all,"coffee_form":form})


def change_coffee(request,name):
    one = get_object_or_404(coffe, name=name)
    if request.method=='DELETE':
        one.delete()
        return redirect('coffee')
    elif request.method=='POST':
        form=coffeForm(request.POST,instance=one)
        if form.is_valid():
            form.save()
            return redirect('coffee')
    form = coffeForm()
    return render(request, 'sujung.html', {"va":one,"c_form": form})


    # return render(request,'coffee.html',{ "coffee_list":coffe_all,"coffee_form":form})