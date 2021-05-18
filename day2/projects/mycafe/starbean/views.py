from django.shortcuts import render


def index(request):
    info = {
        "name": "MEI Y.",
        "email": "devmei.n@gmail.com",
        "majors": ["Physics", "ICEE(Information, Communications and Electronic Engineering)"],
        "skills": ["JS", "Java", "python", "C"],
        "studying": ["Statistics and Data Science", "AI"]
    }
    return render(request, 'index.html', info)
