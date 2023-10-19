from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from datetime import date

from .models import Company, ReferenceEmployee
from .forms import CustomUserForm


def index(request):
    companies = Company.objects.all()

    data = {
        'companies': companies
    }

    return render(request, 'reference/home.html', data)


def company(request, id_company):
    references = ReferenceEmployee.objects.filter(
        employee__company_name=id_company,
        date_end__lt=date.today(),
        employee__status=True
    )
    company_name = get_object_or_404(Company, pk=id_company)

    data = {
        'company_name': company_name,
        'references': references,
        'title_table': ['ФИО', 'Дата рождения', 'Справка', 'Срок']
    }

    return render(request, 'reference/company.html', data)


def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(index)
    else:
        form = CustomUserForm()

    return render(request, 'reference/register.html', {'form': form})


def page_not_found(request, exception):
    return redirect(index)
