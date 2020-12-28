import json

from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Coffee, Phone, PhoneCompany
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
    context_dict = {}

    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('homepage:phone'))

    context_dict['phone_list'] = Phone.objects.all()
    context_dict['phone_form'] = PhoneForm()
    return render(request, 'phone.html', context_dict)


@csrf_exempt
def phone_pk_view(request, **kwargs):

    if request.method == "DELETE":
        try:
            phone = Phone.objects.get(pk=kwargs['pk'])
        except (KeyError, Phone.DoesNotExist):
            return JsonResponse({'msg': 'id 값이 올바르지 않습니다!'}, status=400)
        else:
            phone.delete()
        return JsonResponse({'msg': '삭제 완료.'}, status=200)

    if request.method == "PUT":
        form_data = QueryDict(request.body)

        try:
            phone = Phone.objects.get(pk=kwargs['pk'])
        except (KeyError, Phone.DoesNotExist):
            return JsonResponse({'msg': 'id 값이 올바르지 않습니다!'}, status=400)
        else:
            phone.name = form_data['name']
            phone.price = form_data['price']
            phone.company = PhoneCompany.objects.get(pk=form_data['company'])
            phone.save()
            form_data = dict(form_data)
            form_data['company_name'] = phone.company.name
            form_data['msg'] = '수정 완료.'
            return JsonResponse(form_data, status=200)
