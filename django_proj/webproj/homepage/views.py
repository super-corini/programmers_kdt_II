from django.shortcuts import render
from .models import Chicken
from .forms import ChickenForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ChickenView(request):
    chicken_all = Chicken.objects.all()

    if request.method == 'POST':
        form = ChickenForm(request.POST)
        if form.is_valid:
            form.save()
    '''
    if request.method == 'PUT':
        form = ChickenForm(request.PUT)
        if form.is_valid:
            form.save()

    if request.method == 'DELETE':
        form = ChickenForm(request.DELETE)
        if form.is_valid:
            form.save()
    '''
    form = ChickenForm()
    return render(request, 'chicken.html', {'chicken_list':chicken_all, 'chicken_form':form})
