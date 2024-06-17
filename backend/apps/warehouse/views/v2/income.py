from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from apps.warehouse.forms.incomes import IncomeForm, IncomeItemsFormSet
from apps.warehouse.models import IncomeModel, CompanyModel, StorePointModel, ItemsModel

from django.shortcuts import render, redirect


def income_view(request):
    incomes = IncomeModel.objects.all()
    context = {
        "incomes": incomes
    }
    return render(request, 'v2/income/income_list.html', context)


#---------------THIS WAS SUCCESSFUL------------------------

# def income_create_view(request):
#     income = get_object_or_404(IncomeModel, pk=1)
#     companies = CompanyModel.objects.all()
#     stores = StorePointModel.objects.all()
#     items = ItemsModel.objects.all()
#
#     user = request.user
#
#     context = {
#         "income": income,
#         "companies": companies,
#         "stores": stores,
#         "details": income.income_items.all(),
#         "items": items
#     }
#     if request.method == 'POST':
#         income = IncomeModel(created_by=user)
#         form = IncomeForm(request.POST or None, request.FILES or None, instance=income)
#         if form.is_valid():
#             form.created_by = user
#             form.save()
#             return redirect('warehouse_v2:v2-mp-income')
#         else:
#             return redirect('warehouse_v2:v2-mp-income')
#     return render(request, 'v2/income/create_income.html', context)

def income_create_view(request):
    # target_income = get_object_or_404(IncomeModel, pk=1)
    companies = CompanyModel.objects.all()
    stores = StorePointModel.objects.all()
    items = ItemsModel.objects.all()

    user = request.user

    if request.method == 'POST':
        income = IncomeModel(created_by=user)
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            income = form.save()
        formset = IncomeItemsFormSet(request.POST)

        if formset.is_valid():
            income = form.save()
            income_items = formset.save(commit=False)
            for item in income_items:
                item.income = income
                item.save()
            return redirect('warehouse_v2:v2-mp-income')  # Replace with your success URL
        else:
            print(formset, '------formset')
            return redirect('warehouse_v2:v2-mp-income')  # Replace with your success URL

    else:
        form = IncomeForm()
        formset = IncomeItemsFormSet()
    context = {
        # "income": target_income,
        "companies": companies,
        "stores": stores,
        # "details": target_income.income_items.all(),
        "items": items,
        'form': form, 'formset': formset
    }
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


