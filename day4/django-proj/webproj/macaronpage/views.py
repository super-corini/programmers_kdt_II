from django.shortcuts import HttpResponse, render
from .models import Macaron

# Create your views here.
def macaron_list(request):
    macaron_all = Macaron.objects.all()
    # # 만약 reqeust가 POST라면:
    # if request.method == "POST":
    #     # POST를 바탕으로 Form을 완성하고
    #     form = CoffeeForm(request.POST)
    #     # Form이 유효하면 -> 저장
    #     if form.is_valid():
    #         form.save()

    # form = CoffeeForm()
    return render(request, 'macarons.html', {'macaron_list' : macaron_all})