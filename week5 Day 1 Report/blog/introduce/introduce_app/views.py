from django.shortcuts import render

def main(request):
    return render(request, 'main.html',{})

def introduce(request):
    return render(request, 'introduce.html', {})

def like(request):
    return render(request, 'like.html', {})

def todo(request):
    return render(request, 'todo.html', {})