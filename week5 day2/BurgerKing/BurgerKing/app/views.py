"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import burgers
from .forms import BurgerForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/IntroPage.html',
        {

        }
    )

def burger(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/BurgerList.html',
        {

        }
    )

def burger_list(request):
    assert isinstance(request, HttpRequest)

    burger_all = burgers.objects.all()

    if request.method == "POST":
        form = BurgerForm(request.POST)
        if form.is_valid():
            form.save()

    form = BurgerForm()
    return render(
        request,
        'app/BurgerList.html',
        {
            "burger_list" : burger_all,
            "burger_form" : form,
        }
    )