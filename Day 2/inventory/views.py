from django.shortcuts import HttpResponse, render

from django.http.response import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError

from .models import Bugger
from .forms import BuggerForm
from .serializers import BurgerSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def bugger_view(request):
    return render(request, 'bugger.html', {"my_list":bugger})

# POST : stock 업데이트 / DELETE : outofstock 

@csrf_exempt
def burger_ud(request, name) :
    obj = Bugger.objects.get(name=name)

    # Update
    if request.method == 'PUT' :
        json_data = JSONParser().parse(request)
        serializer = GameSerializer(obj, data = json_data)
        if serializer.is_valid() :
            serializer.save()
        else :
            return JsonResponse(serializer.errors, status=400)

    # Delete
    elif request.method == 'DELETE' :
        obj.delete()

    # Read One Object 
    elif request.method == 'GET' :
        serializer = BurgerSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    else :
        return JsonResponse({'message' : 'Bad Request'}, status=400)

    return redirect('/burger')