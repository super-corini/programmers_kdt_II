from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Coffee
from .forms import CoffeeForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello 야옹!</h1>')
    # render(request, '.html', {})
    birth = "2013/04/13"
    name = "야옹이/meow"
    return render(request, 'index.html', {"cat_birth": birth, "cat_name": name})

@method_decorator(csrf_exempt)
def coffee_view(request):
    # 만약 request == POST:
        # POST를 바탕으로 Form을 완성하고,
        # Form이 유효하면 -> 저장!
    if request.method == "POST":
        form = CoffeeForm(request.POST) # 완성된 Form
        if form.is_valid(): # 채워진 Form이 유효하다면
            form.save() # From 내용을 Model에 저장
        return redirect('/coffee')
    elif request.method == "GET":
        coffee_all = Coffee.objects.all()
        form = CoffeeForm()
        return render(request,'coffee.html',{"coffee_list": coffee_all, "coffee_form": form})


def coffee_edit(request, pk): # 수정을 위한 함수
    coffee = get_object_or_404(Coffee,pk=pk) # pk에 해당하는 객체를 가져온다

    if request.method=='POST': # POST request가 들어오면
        form = CoffeeForm(request.POST, instance=coffee) # 수정할 Data가 valid한지 check하고
        if form.is_valid():
            form.save()
        return redirect('/coffee') # 원래 커피 목록으로 return
    else: # POST가 아니면
        form = CoffeeForm(instance=coffee) # edit 페이지를 연다.
        return render(request, 'coffee_edit.html', {'coffee_form': form})



def coffee_delete(request, pk): ## pk에 해당하는 객체를 삭제한다.
    coffee = Coffee.objects.get(pk=pk)
    coffee.delete()
    return redirect('/coffee')
