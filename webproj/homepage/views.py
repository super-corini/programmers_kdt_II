from django.shortcuts import render
from .models import Coffee, Phone
from .forms import CoffeeForm, PhoneForm


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def coffee_view(request):
    coffee_all = Coffee.objects.all()  # get(), fileter(), ...

    # 만약 request가 POST라면:
    # POST를 바탕으로 Form을 완성하고
    # Form이 유효하면 -> 저장!
    if request.method == "POST":
        form = CoffeeForm(request.POST)  # 내용이 채워진 완성된 Form
        if form.is_valid():  # 채워진 Form이 유효하다면:
            form.save()  # Form 내용을 Model에 저장

    form = CoffeeForm()
    return render(request, 'coffee.html', {'coffee_list': coffee_all, 'coffee_form': form})


def phone_view(request):
    phone_all = Phone.objects.all()

    if request.method == "POST":
        form = PhoneForm(request.POST)  # 내용이 채워진 완성된 Form
        if form.is_valid():  # 채워진 Form이 유효하다면:
            form.save()  # Form 내용을 Model에 저장

    form = PhoneForm()
    return render(request, 'phone.html', {'phone_list': phone_all, 'phone_form': form})
