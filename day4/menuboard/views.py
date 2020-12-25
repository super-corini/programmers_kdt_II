from django.shortcuts import render, redirect
from .models import Fruit
from .forms import FruitForm
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET

# Create your views here.
@require_GET
def profile(request):
    return render(request, 'menuboard/profile.html')


# fruit Board

# Create, Read
@require_http_methods(['GET', 'POST'])
def fruit_create_read(request):
    # Create
    if request.method == "POST":
        # request.FILES 필수!
        form = FruitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menuboard:fruit_create_read')
    # Read
    fruits = Fruit.objects.all()
    context = {
        'fruits': fruits,
        'create_form': FruitForm(),
    }
    return render(request, 'menuboard/fruitlist.html', context)


# Update, Delete
@require_http_methods(['PUT', 'DELETE'])
def fruit_update_delete(request, pk):
    fruit = get_object_or_404(Fruit, pk=pk)
    # Update
    if request.method == "PUT":
        pass
    elif request.method == "DELETE":
        fruit.delete()
        return redirect('menuboard:menu_create_read')