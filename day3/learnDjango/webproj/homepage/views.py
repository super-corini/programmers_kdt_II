from django.shortcuts import HttpResponse, render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Lol
from .forms import LolForm


# Create your views here.
def index(request): # / 일때 실행
    name = "Ahn Doheon"
    nums = [1,2,3,4,5]

    return render(request, 'index.html', {"my_name":name, "my_list":nums})

@method_decorator(csrf_exempt, name = "dispatch")
class Lolview(View):

    def get(self, request):
        lolchamp_all = Lol.objects.all()
        form = LolForm()
        return render(request, 'lol.html', {"lolchamp_list":lolchamp_all, "lolchamp_form":form})

    def post(self, request):
        method = request.POST.get('_method','')
        if method == 'put':
            return self.put(request, request.POST['id'])
        if method == 'delete':
            return self.delete(request, request.POST['id'])
        lolchamp = Lol.objects.all()
        form = LolForm(request.POST)
        if form.is_valid():
            form.save()
            
        form = LolForm()
        return render(request, 'lol.html', {"lolchamp_list":lolchamp, "lolchamp_form":form}) 

    def put(self, request, pk):
        change = Lol.objects.get(pk = pk)
        form = LolForm(request.POST, instance=change)
        if form.is_valid():
            form.save()
        return redirect('/lol')
    def delete(self, request, pk):
        delete = Lol.objects.get(id = pk)
        delete.delete()
        return redirect('/lol')
    


def coffee_view(request): # /coffee 일때 실행
    coffee_all = Coffee.objects.all() #.get(), .filter(),

    #만약 request가 POST라면 POST를 바탕으로 Form을 완성하고 form이 유효하면 저장
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()

    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list":coffee_all, "coffee_form":form}) 