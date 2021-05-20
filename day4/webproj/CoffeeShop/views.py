from django.shortcuts import render
from CoffeeShop.models import Coffee
from CoffeeShop import forms

# Create your views here.
def all_coffee_list(request):
    my_coffee_list = Coffee.objects.order_by('id')
    dict = {"my_coffee_list":my_coffee_list}
    return render(request, 'CoffeeShop/all_coffee_list.html', dict)

def coffee_PD(request, coffee_id):
    data = Coffee.objects.get(pk=coffee_id)
    dict = {'title':"List of Coffees",'coffee':data}
    return render(request, 'CoffeeShop/coffee_PD.html',context=dict)

def coffee_form(request):
    new_form = forms.CoffeeForm()

    if request.method == "POST":
        new_form = forms.CoffeeForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return all_coffee_list(request) # show coffee list
    dict = {'coffee_form':new_form, 'heading_1':'Add New Coffee'}

    return render(request, 'CoffeeShop/coffees_form.html', dict)

def edit(request):
    new_form = forms.CoffeeForm()
    dict = {'edit_form':new_form}
    return render(request, 'CoffeeShop/coffees_PD.html',context=dict)