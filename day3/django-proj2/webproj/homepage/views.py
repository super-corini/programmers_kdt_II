# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    nums = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {"my_list" : nums})