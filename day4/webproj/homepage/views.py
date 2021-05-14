from django.shortcuts import render

# Create your views here.
def index(request):
    name = "Hwangwoojin"
    age = 25
    doing = "KDT Programmers AI"
    render_dict = {
        "name": name,
        "age": age,
        "doing": doing
    }
    return render(request, 'index.html', render_dict)