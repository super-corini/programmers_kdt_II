from django.shortcuts import HttpResponse, render

# Create your views here.


def index(request):
    name ="Miclael"
    nums=[1,2,3,4,5]
    return render(request,'index.html',{'my_name':name,"mylist":nums})
    #return HttpResponse("<h1>Hello World!</h1>")

def hello(request):
    name='Lee chang hyeon'
    age =28
    living_area ='cheonggu'
    return render(request,'hello.html',{'my_name':name,'my_age':age,
                                        'my_living_area':living_area})
