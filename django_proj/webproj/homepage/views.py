from django.shortcuts import render

# Create your views here.
def introduce(request):
    return render(request, 'introduce/introduce_myself.html', {})