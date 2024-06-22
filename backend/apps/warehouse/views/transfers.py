from operator import attrgetter

from django.core.paginator import EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from apps.warehouse.forms.transfers import TransferForm, VariantFormSet
from apps.warehouse.models import ItemsModel
from apps.warehouse.models import SendRegistryModel
from apps.warehouse.models import StorePointModel

ITEMS_PER_PAGE = 30


def transfers_view(request):
    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')
    if search_query:
        transfers = sorted(get_transfers_queryset(search_query), key=attrgetter('created_at'), reverse=True)
    else:
        transfers = sorted(get_transfers_queryset(query), key=attrgetter('created_at'), reverse=True)

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
    return render(request, 'transfers/transfers_list.html', context)


def transfers_detailed_view(request, pk):
    transfer = get_object_or_404(SendRegistryModel, pk=pk)
    context = {
        "transfer": transfer,
        "details": transfer.send_registry_items.all()
    }
    return render(request, 'transfers/transfer_details.html', context)


class TransferInline():
    form_class = TransferForm
    model = SendRegistryModel
    template_name = "transfers/transfer_create.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.sender_id = 1
        self.object.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.transfers():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('warehouse_v2:transfers')

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
            variant.created_by = self.request.user
            variant.save()


class TransferCreate(TransferInline, CreateView):
    def get_context_data(self, **kwargs):
        receivers = StorePointModel.objects.all()
        stores = StorePointModel.objects.all()
        transfers = ItemsModel.objects.all()

        ctx = super(TransferCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        ctx['companies'] = receivers
        ctx['stores'] = stores
        ctx['transfers'] = transfers

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


class TransferUpdate(TransferInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(TransferUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
        }


def get_transfers_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        transfers = SendRegistryModel.objects.filter(
                Q(series__icontains=q) |
                Q(receiver__name__icontains=q) |
                Q(state__icontains=q)
            ).distinct()
        for new in transfers:
            queryset.append(new)

    return list(set(queryset))