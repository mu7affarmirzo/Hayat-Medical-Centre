# views.py
from django.shortcuts import render, redirect

from apps.warehouse.forms import IncomeForm, IncomeItemsFormSet
from apps.warehouse.models import IncomeModel, ItemsModel

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


def item_search(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        items = ItemsModel.objects.filter(name__icontains=query)
        results = [{'id': item.id, 'name': item.name, 'price': item.price} for item in items]
        return JsonResponse(results, safe=False)
    return JsonResponse({'error': 'No query provided'}, status=400)
