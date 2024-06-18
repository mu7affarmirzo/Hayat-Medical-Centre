from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, UpdateView

from apps.warehouse.models import SendRegistryModel


from apps.warehouse.forms.transfers import TransferForm, VariantFormSet
from apps.warehouse.models import CompanyModel, StorePointModel, ItemsModel


def transfers_view(request):
    transfers = SendRegistryModel.objects.all()
    context = {
        "transfers": transfers
    }
    return render(request, 'v2/transfers/transfers_list.html', context)


def transfers_detailed_view(request, pk):
    transfer = get_object_or_404(SendRegistryModel, pk=pk)
    context = {
        "transfer": transfer,
        "details": transfer.send_registry_items.all()
    }
    return render(request, 'v2/transfers/transfer_details.html', context)


class TransferInline():
    form_class = TransferForm
    model = SendRegistryModel
    template_name = "v2/transfers/transfer_create.html"

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
        for name, formset in named_formsets.items():
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
        items = ItemsModel.objects.all()

        ctx = super(TransferCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        ctx['companies'] = receivers
        ctx['stores'] = stores
        ctx['items'] = items

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
