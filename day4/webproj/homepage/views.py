from django.shortcuts import HttpResponse, render
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