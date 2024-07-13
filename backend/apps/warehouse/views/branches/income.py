from operator import attrgetter

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView

from apps.account.models import NotificationModel
from apps.warehouse.forms.branch.incomes import AcceptIncomesForm, AcceptVariantForm, AcceptVariantFormSet
from apps.warehouse.models import SendRegistryModel
from apps.warehouse.models.store_point import StorePointStaffModel

ITEMS_PER_PAGE = 30


@login_required(login_url="warehouse_v2:login")
def branch_income_view(request):
    staff = request.user
    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')

    store_point = StorePointStaffModel.objects.filter(staff=staff)
    if not store_point:
        logout(request)
        return redirect('warehouse_v2:login')

    store_point = store_point.first()

    if search_query:
        incomes = sorted(get_transfers_queryset(store_point.store_point, search_query), key=attrgetter('created_at'), reverse=True)
    else:
        incomes = sorted(get_transfers_queryset(store_point.store_point, query), key=attrgetter('created_at'), reverse=True)

    page = request.GET.get('page', 1)
    incomes_paginator = Paginator(incomes, ITEMS_PER_PAGE)

    try:
        incomes = incomes_paginator.page(page)
    except PageNotAnInteger:
        incomes = incomes_paginator.page(ITEMS_PER_PAGE)
    except EmptyPage:
        incomes = incomes_paginator.page(incomes_paginator.num_pages)

    context = {
        "incomes": incomes
    }
    notifications = NotificationModel.objects.filter(receiver=request.user, state=False)
    context['notifications'] = notifications

    return render(request, 'branches/income_list.html', context)


@login_required(login_url="warehouse_v2:login")
def detailed_income_view(request, pk):
    income = get_object_or_404(SendRegistryModel, pk=pk)
    notifications = NotificationModel.objects.filter(receiver=request.user, state=False)

    context = {
        "income": income,
        "notifications": notifications,
        "details": income.send_registry_items.all()
    }

    return render(request, 'branches/income_details.html', context)


class IncomeInline:
    form_class = AcceptIncomesForm
    model = SendRegistryModel
    template_name = "branches/income_update.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        store_point = StorePointStaffModel.objects.filter(staff=self.request.user)

        store_point = store_point.first()
        warehouse = store_point.store_point

        self.object = form.save(commit=False)
        self.object.modified_by = self.request.user
        self.object.receiver = warehouse
        print(self.object.state, '-checking', form.cleaned_data['state'])
        self.object.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('warehouse_branch:income-list')

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
            variant.send_registry = self.object
            variant.modified_by = self.request.user
            print(variant.state)
            variant.save()


class IncomeCreate(IncomeInline, CreateView):
    def get_context_data(self, **kwargs):

        ctx = super(IncomeCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()

        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': AcceptVariantFormSet(prefix='variants'),
            }
        else:
            return {
                'variants': AcceptVariantFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
            }


class IncomeUpdate(IncomeInline, UpdateView):

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     print(instance.state)
    #     instance.save()
    #     # super(IncomeUpdate, self).save(form)
    #     return HttpResponseRedirect(self.get_success_url())

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.state == 'доставлено':
            return redirect('warehouse_branch:income-list')
        return super(IncomeUpdate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(IncomeUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': AcceptVariantFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
        }


def get_transfers_queryset(store_point, query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        transfers = SendRegistryModel.objects.filter(receiver=store_point).filter(
                Q(series__icontains=q) |
                Q(receiver__name__icontains=q) |
                Q(state__icontains=q)
            ).distinct()
        for new in transfers:
            queryset.append(new)

    return list(set(queryset))