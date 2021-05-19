from django.shortcuts import render, redirect
from django.views import generic

from .models import Company
from .forms import CompanyForm


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def companies(request):
    company_all = Company.objects.all()

    if request.method == "POST":
        company_form = CompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()

    company_form = CompanyForm()
    return render(request, 'company_list.html', {'companies': company_all, 'company_form': company_form})


def company(request, pk):
    cpn = Company.objects.get(pk=pk)
    val = 'init'
    return render(request, 'company.html', {'company': cpn, 'val': val})


def delete_company(request, pk):
    cpn = Company.objects.get(pk=pk)

    if request.method == "POST":
        cpn.delete()
        return redirect('../companies/')

    return render(request, 'none.html', {})


def modify_company(request, pk):
    cpn = Company.objects.get(pk=pk)
    company_form = CompanyForm(instance=cpn)

    if request.method == "POST":
        company_form = CompanyForm(request.POST, instance=cpn)
        company_form.save()
        return redirect('../companies/')

    return render(request, 'none.html', {'company_form': company_form})
