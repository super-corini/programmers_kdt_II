from django.shortcuts import HttpResponse, render, redirect
from django.views.generic import View  # CRUD method 구별

from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    #return HttpResponse("Hello world!")
    return render(request,'index.html',{})

def coffee_view(request):
    coffee_all = Coffee.objects.all() # get() ... filter()... 
    
    # 만약 request가 POST이면:
        # POST 바탕으로 FORM을 완성
        # FORM이 유효하면 저장!
    
    if request.method == 'POST':
        form = CoffeeForm(request.POST) # 빈 인자가 아닌 request.POST로 완성된 Form을 저장
        if form.is_valid() : # 채워진 Form이 유효하다면
            form.save()  # meta 클래스에 해당 로직을 지정해놓았음.

    form = CoffeeForm()

    return render(request,'coffee.html',{ 'coffee_list' : coffee_all , 'coffee_form' : form} )

def coffee_edit(request, pk):
    
    coffee_select = Coffee.objects.get(pk=pk)  # django ORM get함수 : 단일행을 조건에 따라 가져올때 사용, cf) filter는 여러행을 조건에 가져올 때 사용

    method = request.POST.get('_method', '') # html form에서 POST method로 보내되 hidden input으로 DELETE를 요청시킴
    if method == 'DELETE' :
        coffee_select.delete()  # get함수로 으로 선택된 메뉴 delete()로 삭제
        return redirect('/coffee')
    
    if method == 'PUT' :
        form = CoffeeForm(request.POST) # 빈 인자가 아닌 request.POST로 완성된 Form을 저장
        if form.is_valid() : # 채워진 Form이 유효하다면 form의 cleaned_data로 key값 넣어주기
            coffee_select.name = form.cleaned_data['name']
            coffee_select.price = form.cleaned_data['price']
            coffee_select.is_ice = form.cleaned_data['is_ice']
            coffee_select.save()

        return redirect('/coffee')

    form = CoffeeForm()
    return render(request,'coffee_edit.html',{ 'coffee_select' : coffee_select , 'coffee_form' : form} )