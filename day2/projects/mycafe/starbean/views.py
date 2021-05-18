from django.shortcuts import render

from .models import Coffees


def index(request):
    info = {
        "name": "MEI Y.",
        "email": "devmei.n@gmail.com",
        "majors": ["Physics", "ICEE(Information, Communications and Electronic Engineering)"],
        "skills": ["JS", "Java", "python", "C"],
        "studying": ["Statistics and Data Science", "AI"]
    }
    return render(request, 'index.html', info)


def coffee_list(request):
    coffees = Coffees.objects.all()
    context = {'coffee_list': coffees}
    return render(request, 'coffee.html', context)
