from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Coffee
from .forms import CoffeeForm


# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'title': '강기주',
        'subTitle': '1기',
        'description': '디...장고',
        'stack': ['React', 'UWP', 'Spring'],
        'location': '서울',
        'lang': '0개 국어',
        'website': '부끄',
    })


class CoffeeView(View):
    def get(self, request):
        return render(request, 'coffee.html', {"coffee_list": Coffee.objects.all()})

    def post(self, request):
        method = self.request.POST.get('_method', '').lower()
        if method == "put":
            return self.put(request, request.POST['id'])
        elif method == "delete":
            return self.delete(request, request.POST['id'])

        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, 'coffee.html', {"coffee_list": Coffee.objects.all()})

    def put(self, request, coffee_id):
        form = CoffeeForm(request.POST, instance=Coffee.objects.get(id=coffee_id))
        form.save()

        return redirect('/coffees')

    def delete(self, request, coffee_id):
        form = get_object_or_404(Coffee, pk=coffee_id)
        form.delete()

        return redirect('/coffees')


def coffee_create(request):
    return render(request, 'coffee_create.html')


def coffee_update(request, coffee_id):
    coffee_instance = get_object_or_404(Coffee, pk=coffee_id)

    return render(request, 'coffee_update.html', {"coffee_info": coffee_instance})
