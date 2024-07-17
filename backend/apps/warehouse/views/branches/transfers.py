from operator import attrgetter

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from apps.warehouse.forms.transfers import VariantFormSet, TransferForm
from apps.warehouse.models import SendRegistryModel, StorePointStaffModel, StorePointModel

ITEMS_PER_PAGE = 30
OUTGOING_PER_PAGE = 30


@login_required
def transfers_view(request):
    staff = request.user
    store_point = StorePointStaffModel.objects.filter(staff=staff)

    if not store_point:
        logout(request)
        return redirect('warehouse_v2:login')

    store_point = store_point.first()
    warehouse = store_point.store_point

    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')
    if search_query:
        transfers = sorted(get_transfers_queryset(warehouse, search_query), key=attrgetter('created_at'), reverse=True)
    else:
        transfers = sorted(get_transfers_queryset(warehouse, query), key=attrgetter('created_at'), reverse=True)

    page = request.GET.get('page', 1)
    transfers_paginator = Paginator(transfers, ITEMS_PER_PAGE)

    try:
        transfers = transfers_paginator.page(page)
    except PageNotAnInteger:
        transfers = transfers_paginator.page(ITEMS_PER_PAGE)
    except EmptyPage:
        transfers = transfers_paginator.page(transfers_paginator.num_pages)

    context = {
        "transfers": transfers
    }
    return render(request, 'branches/transfers-list.html', context)


@login_required
def transfers_detailed_view(request, pk):
    return render(request, 'branches/transfers-list.html', {})


class TransferInline:
    form_class = TransferForm
    model = SendRegistryModel
    template_name = "branches/transfer_create.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        store_point = StorePointStaffModel.objects.filter(staff=self.request.user)

        store_point = store_point.first()
        warehouse = store_point.store_point

        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.sender = warehouse
        self.object.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('warehouse_branch:transfers-list')

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
            print(self.object)
            variant.send_registry = self.object
            variant.created_by = self.request.user
            variant.save()


class TransferCreate(TransferInline, CreateView):
    def get_context_data(self, **kwargs):
        receivers = StorePointModel.objects.all()
        stores = StorePointModel.objects.all()

        ctx = super(TransferCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        ctx['companies'] = receivers
        ctx['stores'] = stores

        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': VariantFormSet(prefix='variants', form_kwargs={'user': self.request.user}),
            }
        else:
            return {
                'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants', form_kwargs={'user': self.request.user}),
            }


class TransferUpdate(TransferInline, UpdateView):
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.state == 'доставлено':
            return redirect('warehouse_branch:transfers-list')
        return super(TransferUpdate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(TransferUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants', form_kwargs={'user': self.request.user}),
        }


def get_transfers_queryset(store_point, query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        transfers = SendRegistryModel.objects.filter(sender=store_point).filter(
                Q(series__icontains=q) |
                Q(receiver__name__icontains=q) |
                Q(state__icontains=q)
            ).distinct()
        for new in transfers:
            queryset.append(new)

    return list(set(queryset))

