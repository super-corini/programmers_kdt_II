from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from ipware import get_client_ip
# Create your views here.

class Index(View):
    def get(self, request):
        ip, is_routable = get_client_ip(request)
        print(ip)
        return HttpResponse("일단 받음")