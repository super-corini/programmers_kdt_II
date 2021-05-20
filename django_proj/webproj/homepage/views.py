from django.shortcuts import HttpResponse, render
from .models import Coffee

from .forms import CoffeeForm, BugerForm
from .model import BugerMaterial

# Create your views here.


def index(request):
    name ="Miclael"
    nums=[1,2,3,4,5]
    return render(request,'index.html',{'my_name':name,"mylist":nums})
    #return HttpResponse("<h1>Hello World!</h1>")

def hello(request):
    name='Lee chang hyeon'
    age =28
    living_area ='cheonggu'
    return render(request,'hello.html',{'my_name':name,'my_age':age,
                                        'my_living_area':living_area})

def coffee_view(request):
    coffee_all = Coffee.objects.all()# coffee object의 모든 것을 가져와!

    #form =CoffeeForm()
    #만약 request가 POST라면 :
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면 -> 저장!
    if request.method== 'POST':
        form = CoffeeForm(request.POST) #완성된 form
        if form.is_valid(): #채워진 Form이 유효하다면
            form.save() # 이 Form 내용을 Model에 저장
    form = CoffeeForm()
    return render(request, 'coffee.html',{'coffee_list':coffee_all, 'coffee_form':form})



def buger_manage(request):
    Buger_all = BugerMaterial.objects.all()# coffee object의 모든 것을 가져와!

    if request.method== 'POST':
        form = BugerForm(request.POST) #완성된 form
        if form.is_valid(): #채워진 Form이 유효하다면
            form.save()

    form = BugerForm()
    return render(request, "buger.html",{'bugermaterial_list':Buger_all, 'bugermaterial_form':form})#, 'bugermaterial_form':form



















