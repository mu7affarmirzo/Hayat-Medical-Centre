# views.py
from django.shortcuts import render, redirect

from apps.warehouse.forms import IncomeForm, IncomeItemsFormSet
from apps.warehouse.models import IncomeModel, ItemsModel, CompanyModel, StorePointModel

from django.http import JsonResponse


def register_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        formset = IncomeItemsFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            print(form)
            income = form.save()
            income_items = formset.save(commit=False)
            for item in income_items:
                item.income = income
                item.save()
            return redirect('success_url')  # Replace with your success URL
        else:
            print('ERROR')
    else:
        form = IncomeForm()
        formset = IncomeItemsFormSet()
    return render(request, 'v2/main_point/test.html', {'form': form, 'formset': formset})


def register_income_dynamic(request):
    companies = CompanyModel.objects.all()
    stores = StorePointModel.objects.all()
    items = ItemsModel.objects.all()

    if request.method == 'POST':
        form = IncomeForm(request.POST)
        formset = IncomeItemsFormSet(request.POST)
        if form.is_valid():
            income = form.save()
        print(len(formset))
        for i in formset:
            print(i.quantity)
        if formset.is_valid():
            print(form)
            income = form.save()
            income_items = formset.save(commit=False)
            for item in income_items:
                item.income = income
                item.save()
            return redirect('success_url')  # Replace with your success URL
        else:
            print(formset.errors)
            print(formset.non_form_errors())
            print('ERROR')
    else:
        form = IncomeForm()
        formset = IncomeItemsFormSet()
    context = {
        "companies": companies,
        "stores": stores,
        "items": items,
        'form': form, 'formset': formset
    }
    return render(request, 'v2/main_point/test_dynamic.html', context)


def item_search(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        items = ItemsModel.objects.filter(name__icontains=query)
        results = [{'id': item.id, 'name': item.name, 'price': item.price,
                    'seria': item.seria, 'company': item.company.name} for item in items]
        print(results)
        return JsonResponse(results, safe=False)
    return JsonResponse({'error': 'No query provided'}, status=400)
