from django.shortcuts import render, redirect
from .models import Fruit
from .forms import FruitForm
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET

# crawling
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote

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
        name = quote(request.POST["name"])
        response = urlopen(f'https://terms.naver.com/search.nhn?query={name}')
        soup = BeautifulSoup(response, 'html.parser')
        request_dict = request.POST.dict()
        request_dict['imgsrc'] = soup.select("div.thumb_area img")[0]["data-src"]
        form = FruitForm(request_dict)
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
# @require_http_methods(['PUT', 'DELETE'])
def fruit_update_delete(request, pk):
    fruit = get_object_or_404(Fruit, pk=pk)
    # Update
    if request.method == "PUT":
        pass
    else:
        fruit.delete()
        print()
        return redirect('menuboard:fruit_create_read')