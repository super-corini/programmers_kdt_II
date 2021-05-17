from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request) :
    name = 'ShowMaker'

    nums = [1,2,3,4,5]
    return render(request, 'index.html', 
        {
            'name' : name, 
            'nums' : nums
        })