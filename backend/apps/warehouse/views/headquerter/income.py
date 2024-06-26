
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from apps.warehouse.forms.incomes import IncomeForm, VariantFormSet
from apps.warehouse.models import IncomeModel, CompanyModel, StorePointModel, ItemsModel

from operator import attrgetter

from django.db.models import Q

from django.core.paginator import EmptyPage, PageNotAnInteger


from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect


INCOMES_PER_PAGE = 30


class ProductInline():
    form_class = IncomeForm
    model = IncomeModel
    template_name = "income/income_create.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()
        self.object.created_by = self.request.user
        self.object.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.incomes():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('warehouse_v2:mp-income')

    def formset_variants_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.income = self.object
            variant.save()


class ProductCreate(ProductInline, CreateView):

    def get_context_data(self, **kwargs):
        companies = CompanyModel.objects.all()
        stores = StorePointModel.objects.all()
        incomes = ItemsModel.objects.all()

        ctx = super(ProductCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        ctx['companies'] = companies
        ctx['stores'] = stores
        ctx['incomes'] = incomes

        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': VariantFormSet(prefix='variants'),
            }
        else:
            return {
                'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
            }


class ProductUpdate(ProductInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
        }


def income_view(request):
    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')

    if search_query:
        incomes = sorted(get_incomes_queryset(search_query), key=attrgetter('created_at'), reverse=True)
    else:
        incomes = sorted(get_incomes_queryset(query), key=attrgetter('created_at'), reverse=True)

    page = request.GET.get('page', 1)
    incomes_paginator = Paginator(incomes, INCOMES_PER_PAGE)

    try:
        incomes = incomes_paginator.page(page)
    except PageNotAnInteger:
        incomes = incomes_paginator.page(INCOMES_PER_PAGE)
    except EmptyPage:
        incomes = incomes_paginator.page(incomes_paginator.num_pages)

    context = {
        "incomes": incomes
    }
    return render(request, 'income/income_list.html', context)


def income_detailed_view(request, pk):
    income = get_object_or_404(IncomeModel, pk=pk)
    context = {
        "income": income,
        "details": income.income_items.all()
    }
    return render(request, 'income/income_details.html', context)


def get_incomes_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        incomes = IncomeModel.objects.filter(
                Q(serial__icontains=q)
            ).distinct()
        for new in incomes:
            queryset.append(new)

    return list(set(queryset))
