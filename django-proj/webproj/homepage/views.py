from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Coffee, Burger, Id_s
from .forms import CoffeeForm, BurgerForm, IdForm
# Create your views here.
def index(request):
    name = "Michael"
    nums = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {"my_list" : nums, 
                                        "my_name" : name})


# template filter 는 변수의 값을 특정 형식으로 변환해줄 때 사용한다.


def coffee_view(request):
    
    # Coffee 모델에 해당하는 데이터베이스에서 모든 object(행) 을 전부 가지고 오라는 의미이다.
    coffee_all = Coffee.objects.all() 
    # all 대신에 .get(), .filter() 와 같이 특정 조건에 맞는 행만 가져올 수 있음

    # Form 객체를 만들어 준다.
    # 만약 request가 POST라면:
        # POST 를 바탕으로 Form 을 완성하고
        # Form 이 유효하면 저장
    if request.method == "POST":
        # html 파일 안에서 post로 보내줬던 내용을 바탕으로 Coffeeform 을 완성시킨것을 form 이라고 하자는 것이다.
        form = CoffeeForm(request.POST) 
        if form.is_valid(): # form 안에 들어가있는 값들이 유효한지를 확인
            form.save() # 이 Form 내용을 Model 에 저장
    form = CoffeeForm() 
    
    if request.method == "PUT":
        form = CoffeeForm(request.PUT)


    return render(request, 'coffee.html', {"coffee_list": coffee_all,
                                             "coffee_form":form })


def introduce_view(request):
    return render(request, 'portfolio.html', {})
    



def burger_view(request):
    if request.method =="POST":
        return redirect('create')
   # if request.method =='GET':
       # id_value = request.GET.get('id_s')
       # return redirect('update' + str(id_value))
   # if request.method == "PUT" :
     #   return update(request, 2)
        
      #  form = IdForm(request.PUT)
      #  ids = Id_s.objects.get(id = form.cleaned_data['id_s'])
      #  if form.is_valid():
           # return redirect('create')
            #return redirect('burger/update/' + str(ids))
    burger_all = Burger.objects.all()
    id_form = IdForm()
    form = BurgerForm()
    return render(request, 'burger.html', {"burger_list": burger_all,
                                                "burger_form": form,
                                                "id_form": id_form})

def create(request):
    if request.method == "POST": # method가 post 일 때
        form = BurgerForm(request.POST)
    
        if form.is_valid(): # form 유효성 검증
            form.save() # 저장
            return redirect('main') # 다시 main 으로
    else:
        form = BurgerForm() # 빈 form 열기
    return render(request, 'create.html', {'burger_form' : form})

def update(request, pk):
    burgers = get_object_or_404(Burger, pk=pk)
    if request.method =='POST':
        form = BurgerForm(request.POST, instance=burgers) # burger 객체 가져오기
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = BurgerForm(instance = burgers) # buger 객체 가져와서 form 을 생성
    return render(request, 'update.html', {'burger_form': form})


def delete(request, pk):
    burgers = Burger.objects.get(pk=pk)
    burgers.delete()
    return redirect('main')