from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'eda_main.html', {})


def analysis(request):
    return render(request, 'analysis.html', {})


def dataset(request):
    return render(request, 'dataset.html', {})
