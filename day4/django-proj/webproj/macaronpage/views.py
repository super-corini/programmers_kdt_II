from django.shortcuts import HttpResponse, render, redirect
from .models import Macaron, Stock
from .forms import MacaronForm

# Create your views here.
def macaron_list(request):

    # 만약 reqeust가 POST라면:
    if request.method == "POST":
        
        # POST를 바탕으로 Form을 완성하고
        form = MacaronForm(request.POST)
        # Form이 유효하면 -> 저장
        if form.is_valid():
            form.save()

    macaron_all = Macaron.objects.all()
    stock_list = Stock.objects.all()

    form = MacaronForm()
    return render(request, 'macarons.html', {'macaron_list' : macaron_all, 'stock_list' : stock_list, 'macaron_form' : form})


def edit(request,id):
    macaron = Macaron.objects.get(id=id)
    if id is not None:
    
        method = request.POST.get('_method', '').lower()
        # print(method)

        if method == 'put':
            # 메뉴 정보 수정
            try:
                name = request.POST.get('name', 'unknown')
                price = request.POST.get('price', 'unknown')
                amount = request.POST.get('amount', 'unknown')

            except KeyError:
                print('error : KeyError')
            
            print(id, name, price, amount)
            macaron.name = name
            macaron.price = price
            macaron.amount = amount
            macaron.save()

        elif method == 'delete':
            # 메뉴 삭제
            print('삭제')
            macaron.delete()
        
        # return render(request, 'macarons.html',{})
    
    return redirect('/macarons/')
        