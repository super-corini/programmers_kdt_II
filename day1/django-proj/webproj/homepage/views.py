from django.shortcuts import redirect, render, HttpResponse
from django.db import connections
from .models import Coffee
from .forms import CoffeeForm, CoffeeDelForm, CoffeePutForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    # return HttpResponse("Hello world!")
    data = {
        'sub_page_name':'home',
        'profile': {
            '이름': '[2기-B]오준석',
            '나이': '비밀',
            '출몰지': '서울 어딘가',
            '코딩실력': 'SUPER-CORINI'
        }
    }
    return render(request, 'index.html', data)

def get_coffees(request):
    coffee_all = Coffee.objects.all()
    # 만약 request가 POST라면:
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면 -> 저장!
    post_form = CoffeeForm(request.POST) # 완성된 Form
    put_form = CoffeePutForm(request.POST) # 완성된 Form
    if request.method == "POST":
        print(request.POST)
        if request.POST.get('_method') not in ['DELETE', 'PUT']:
            if post_form.is_valid(): # 채워진 Form이 유효하다면
                post_form.save() # 이Form 내용을 model에 저장
    data = {
        'coffees':coffee_all,
        'coffee_form': post_form,
        'put_form': put_form,
        }
    return render(request, 'coffee.html', data)

@csrf_exempt
def other_coffees(request, pk): # PUT, DELETE method 처리
    print('other_coffees', pk)
    print(request.POST.get('_method'))
    if request.method == "POST":
        if request.POST.get('_method') == 'DELETE':
            Coffee.objects.get(id=pk).delete()
        elif request.POST.get('_method') == 'PUT':
            old_obj = Coffee.objects.filter(id=pk).update(
                name = request.POST.get('name'),
                price = int(request.POST.get('price')),
                is_ice = True if request.POST.get('is_ice') else False, 
                is_caffein = True if request.POST.get('is_caffein') else False,
                img_url = request.POST.get('img_url')
            )
            
            # old_obj.name = request.POST.get('name')[0]
            # old_obj.price = int(request.POST.get('price')[0])
            # old_obj.is_ice = True if request.POST.get('is_ice') else False
            # old_obj.is_caffein = True if request.POST.get('is_caffein') else False
            # old_obj.img_url = request.POST.get('img_url')[0]
            # old_obj.save()
    return redirect('/coffees')
    # if request.method == "PUT":
        
