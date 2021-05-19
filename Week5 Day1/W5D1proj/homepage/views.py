from django.shortcuts import render,HttpResponse

def introduce(request):
    if request.method == 'GET':
        return render(request,'introduce.html',{})
    elif request.method == 'POST':
        return HttpResponse("HELLO")
    

