from django.shortcuts import HttpResponse, render
from datetime import datetime


def home(request):
    return render(request, 'home.html', {})


def about(request):
    my_info = {
        "name": "이수진",
        "age": datetime.now().year - 1995 + 1,
        "email": "dltnwls9623@gmail.com",
        "github": "https://github.com/dltnwls9623",
        "blog": "https://velog.io/@pengu",
        "skills": ['Python', 'JAVA', 'C', 'Keras', 'Tensorflow'],
        "research": ['Computer Vision', 'Deep Learning', 'Video Captioning'],
        "education": ['[2014.03 ~ 2017.08] 경기대학교 컴퓨터과학과','[2017.09 ~ 2019.08] 경기대학교 일반대학원']
    }
    return render(request, 'about.html', my_info)


def project(request):
    my_info = {
        "name": "이수진",
        "age": datetime.now().year - 1995 + 1,
        "email": "dltnwls9623@gmail.com",
        "github": "https://github.com/dltnwls9623",
        "blog": "https://velog.io/@pengu",
        "skills": ['Python', 'JAVA', 'C', 'Keras', 'Tensorflow'],
        "research": ['Computer Vision', 'Deep Learning', 'Video Captioning'],
        "education": ['[2014.03 ~ 2017.08] 경기대학교 컴퓨터과학과','[2017.09 ~ 2019.08] 경기대학교 일반대학원']
    }
    return render(request, 'project.html', my_info)


def interests(request):
    my_info = {
        "name": "이수진",
        "age": datetime.now().year - 1995 + 1,
        "email": "dltnwls9623@gmail.com",
        "github": "https://github.com/dltnwls9623",
        "blog": "https://velog.io/@pengu",
        "skills": ['Python', 'JAVA', 'C', 'Keras', 'Tensorflow'],
        "research": ['Computer Vision', 'Deep Learning', 'Video Captioning'],
        "education": ['[2014.03 ~ 2017.08] 경기대학교 컴퓨터과학과','[2017.09 ~ 2019.08] 경기대학교 일반대학원']
    }
    return render(request, 'interests.html', my_info)


