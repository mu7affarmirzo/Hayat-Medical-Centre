
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from apps.account.models import Account
from apps.warehouse.forms.expanses import ExpanseForm, VariantFormSet
from apps.warehouse.models import ExpenseModel, CompanyModel, StorePointModel, ItemsModel, ExpenseModel

from operator import attrgetter

from django.db.models import Q

from django.core.paginator import EmptyPage, PageNotAnInteger


from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect


INCOMES_PER_PAGE = 30


class ExpanseInline():
    form_class = ExpanseForm
    model = ExpenseModel
    template_name = "expanses/expanse_create.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()
        self.object.created_by = self.request.user
        self.object.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('warehouse_v2:expanses')

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
            variant.expense = self.object
            variant.save()


class ExpanseCreate(ExpanseInline, CreateView):

    def get_context_data(self, **kwargs):
        receivers = Account.objects.all()

        ctx = super(ExpanseCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        ctx['receivers'] = receivers

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


class ExpanseUpdate(ExpanseInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(ExpanseUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
        }


def expanses_view(request):
    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')

    if search_query:
        expanses = sorted(get_expanses_queryset(search_query), key=attrgetter('created_at'), reverse=True)
    else:
        expanses = sorted(get_expanses_queryset(query), key=attrgetter('created_at'), reverse=True)

    page = request.GET.get('page', 1)
    expanses_paginator = Paginator(expanses, INCOMES_PER_PAGE)

    try:
        expanses = expanses_paginator.page(page)
    except PageNotAnInteger:
        expanses = expanses_paginator.page(INCOMES_PER_PAGE)
    except EmptyPage:
        expanses = expanses_paginator.page(expanses_paginator.num_pages)

    context = {
        "expanses": expanses
    }
    return render(request, 'expanses/expanse_list.html', context)


def expanses_detailed_view(request, pk):
    expanses = get_object_or_404(ExpenseModel, pk=pk)
    context = {
        "expanses": expanses,
        "details": expanses.expanse_items.all()
    }
    return render(request, 'expanses/expanse_details.html', context)


def get_expanses_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        expanses = ExpenseModel.objects.filter(
                Q(series__icontains=q)
            ).distinct()
        for new in expanses:
            queryset.append(new)

    return list(set(queryset))
