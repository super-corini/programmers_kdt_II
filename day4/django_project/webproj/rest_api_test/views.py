## 아직 rest_api_test의 template은 연결하지 않았음
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views import View

# Create your views here.
class IndexView(View):
	# def get(self, request):
	# 	return HttpResponse(index2.html)

	def post(self, request):
		return HttpResponse("Post 요청을 잘 받았다")

	def put(self, request):
		return HttpResponse("Put 요청을 잘 받았다")

	def delete(self, requset):
		return HttpResponse("Delete 요청을 잘 받았다.")