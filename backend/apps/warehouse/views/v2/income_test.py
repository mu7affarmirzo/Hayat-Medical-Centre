from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView

from apps.warehouse.forms.income_test import ProductForm, VariantFormSet
from apps.warehouse.models import IncomeModel, CompanyModel, StorePointModel, ItemsModel


class ProductInline():
    form_class = ProductForm
    model = IncomeModel
    template_name = "v2/income/income_create_test_3.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
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
        items = ItemsModel.objects.all()

        ctx = super(ProductCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        ctx['companies'] = companies
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


class ProductUpdate(ProductInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
        }
