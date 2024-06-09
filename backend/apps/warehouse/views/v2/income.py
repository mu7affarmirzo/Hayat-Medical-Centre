from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from apps.warehouse.forms.incomes import IncomeForm, IncomeItemsFormSet
from apps.warehouse.models import IncomeModel, CompanyModel, StorePointModel


def income_view(request):
    incomes = IncomeModel.objects.all()
    context = {
        "incomes": incomes
    }
    return render(request, 'v2/income/income_list.html', context)


def income_create_view(request):
    income = get_object_or_404(IncomeModel, pk=1)
    companies = CompanyModel.objects.all()
    stores = StorePointModel.objects.all()

    user = request.user

    context = {
        "income": income,
        "companies": companies,
        "stores": stores,
        "details": income.income_items.all()
    }
    if request.method == 'POST':
        income = IncomeModel(created_by=user)
        print(request.POST)
        form = IncomeForm(request.POST or None, request.FILES or None, instance=income)
        formset = IncomeItemsFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            form.save()
            income_items = formset.save(commit=False)
            for item in income_items:
                item.income = income
                item.save()
            return redirect('warehouse_v2:v2-mp-income')
    return render(request, 'v2/income/create_income.html', context)


def income_detailed_view(request, pk):
    income = get_object_or_404(IncomeModel, pk=pk)
    context = {
        "income": income,
        "details": income.income_items.all()
    }
    return render(request, 'v2/income/income_details.html', context)


def load_delivery_companies(request):
    company_id = request.GET.get('company_id')
    companies = CompanyModel.objects.filter(pk=company_id).all()
    return render(request, 'v2/income/create_income.html', {'companies': companies})
