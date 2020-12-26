from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def coffee_view(request):
    coffee_all = Coffee.objects.all()
    # 만약 request가 POST라면:
        # POST를 바탕으로 Form을 완성하고
        # Form이 유효하면 -> 저장!
    """ 임시로 지움
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():  # 채워진 Form이 유효하다면
            form.save()  # 이 Form 내용을 Model에 저장
    """
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()


    form = CoffeeForm()
    return render(request, 'coffee.html',
                  {
                      'coffee_list': coffee_all,
                      'coffee_form': form,
                  }
                  )

def coffee_delete(request, pk):
    coffee_post = Coffee.objects.get(pk=pk)
    coffee_post.delete()
    return redirect('coffee_shop')
