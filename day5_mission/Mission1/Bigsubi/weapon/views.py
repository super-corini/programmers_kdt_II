from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Weapon
import json

# Create your views here.
class IndexView(View):
    def get(self, request):
        temp = {
            "name" : "KyubumShin"
        }
        return JsonResponse(temp)

def Return_Str(request):
    print(request)
    value = request.GET['string']
    temp = {
        "value" : value
    }
    return JsonResponse(temp)

class Weapon_admin(View):
    def get(self, request):
        weapon_all = Weapon.objects.all()
        return JsonResponse({"weapon_list" : [{"name" : weapons.name, "stock" : weapons.stock} for weapons in weapon_all]})

    def post(self, request):
        request = json.loads(request.body)
        Weapon(
            name = request["name"],
            stock = request["stock"]
        ).save()
        weapon_all = Weapon.objects.all()
        return JsonResponse({"weapon_list" : [{"name" : weapons.name, "stock" : weapons.stock} for weapons in weapon_all]})

    
    def put(self, request):
        request = json.loads(request.body)
        weapon = get_object_or_404(Weapon, name = request['name'])
        weapon.stock = request['stock']
        weapon.save()
        weapon_all = Weapon.objects.all()
        return JsonResponse({"weapon_list" : [{"name" : weapons.name, "stock" : weapons.stock} for weapons in weapon_all]})
    
    def delete(self, request):
        request = json.loads(request.body)
        weapon = get_object_or_404(Weapon, name = request["name"])
        weapon.delete()
        weapon_all = Weapon.objects.all()
        return JsonResponse({"weapon_list" : [{"name" : weapons.name, "stock" : weapons.stock} for weapons in weapon_all]})
