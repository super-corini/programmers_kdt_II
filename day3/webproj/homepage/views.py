from django.shortcuts import HttpResponse, render, redirect
from .models import Coffee, Chicken
from .forms import CoffeeForm, ChickenForm

from .serializers import CoffeeSerializer
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Create your views here.
def index(request):
    nums = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {"my_list" : nums})

@api_view(['GET', 'POST'])
def coffee_view(request):
    coffee_all = Coffee.objects.all()

    #만약 request가 POST라면: 
        #POST를 바탕으로 Form을 완성 
        #Form이 유효하면 -> 저장하기
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save() # Form 을 모델에 연동해 저장 
        
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list" : coffee_all , "coffee_form" : form})

@api_view(['GET', 'PUT', 'DELETE'])
def coffee_update_view(request, pk):
    coffee_all = Coffee.objects.all()
    try: 
        coffee = Coffee.objects.get(pk=pk) 
    except Coffee.DoesNotExist: 
        return JsonResponse({'message': 'The coffee does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        coffee_serializer = CoffeeSerializer(coffee) 
        return JsonResponse(coffee_serializer.data) 
    elif request.method == "PUT":
        coffee_data = JSONParser().parse(request) 
        coffee_serializer = CoffeeSerializer(coffee, data=coffee_data) 
        if coffee_serializer.is_valid(): 
            coffee_serializer.save() 
            coffee_all = Coffee.objects.all()
            form = CoffeeForm()
            return render(request, 'coffee.html', {"coffee_list" : coffee_all , "coffee_form" : form})
        return JsonResponse(coffee_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == "DELETE":
        coffee.delete() 
        return JsonResponse({'message': 'Coffee was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    coffee_all = Coffee.objects.all()
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list" : coffee_all , "coffee_form" : form})

def chicken_view(request):
    chicken_list = []
    chicken_all = Chicken.objects.all()
    return render(request, 'chicken.html', {"chicken_list" : chicken_all })
    


def intro(request):
    return render(request, 'introduce.html', {})


