import json
import datetime
import os
from operator import attrgetter

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, CreateView

from apps.account.models import PatientModel
from apps.logus.forms.booking import PatientRegistrationForm
from apps.warehouse.forms.cheque import ChequeItemCountForm, VariantFormSet, ChequeForm
from apps.warehouse.models import WarehouseChequeModel, ChequeItemsModel, ItemsInStockModel

ITEMS_PER_PAGE = 30


class ChequeInline:
    form_class = ChequeForm
    model = WarehouseChequeModel
    template_name = "cheque/cheque_create.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()
        self.object.created_by = self.request.user
        self.object.save()

        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('warehouse_v2:cheque')

    def formset_variants_valid(self, formset):
        variants = formset.save(commit=False)

        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.cheque = self.object
            variant.save()


class ChequeCreate(ChequeInline, CreateView):

    def get_context_data(self, **kwargs):

        ctx = super(ChequeCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        ctx['patients'] = PatientModel.objects.all()

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


class ChequeUpdate(ChequeInline, UpdateView):

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.state == 'оплачено':
            return redirect('warehouse_v2:cheque')
        return super(ChequeUpdate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(ChequeUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        ctx['patients'] = PatientModel.objects.all()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants', form_kwargs={'user': self.request.user}),
        }

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save(commit=False)  # Do not commit to the database yet
        self.object.created_by = self.request.user
        self.object.save()  # Save the instance now

        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()

        return redirect('warehouse_v2:cheque')

    def formset_variants_valid(self, formset):
        variants = formset.save(commit=False)

        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.cheque = self.object  # Associate the existing cheque
            variant.save()


def create_cheque(request):
    if request.method == 'POST':
        form = ChequeForm(request.POST)
        formset = VariantFormSet(request.POST, request.FILES, prefix='variants', form_kwargs={'user': request.user})

        if form.is_valid() and formset.is_valid():
            cheque = form.save(commit=False)
            cheque.created_by = request.user
            cheque.save()

            variants = formset.save(commit=False)
            for variant in variants:
                variant.cheque = cheque
                variant.save()

            for obj in formset.deleted_objects:
                obj.delete()

            return redirect('warehouse_v2:cheque')
    else:
        form = ChequeForm()
        formset = VariantFormSet(prefix='variants', form_kwargs={'user': request.user})

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'cheque/cheque_create.html', context)


def cheque_view(request):
    query = request.GET.get('q', '')
    search_query = request.GET.get('table_search')
    if search_query:
        cheques = sorted(get_cheques_queryset(search_query), key=attrgetter('created_at'), reverse=True)
    else:
        cheques = sorted(get_cheques_queryset(query), key=attrgetter('created_at'), reverse=True)

    page = request.GET.get('page', 1)
    cheques_paginator = Paginator(cheques, ITEMS_PER_PAGE)

    try:
        cheques = cheques_paginator.page(page)
    except PageNotAnInteger:
        cheques = cheques_paginator.page(ITEMS_PER_PAGE)
    except EmptyPage:
        cheques = cheques_paginator.page(cheques_paginator.num_pages)
    context = {
        "cheques": cheques
    }
    return render(request, 'cheque/cheque_list.html', context)


def cheque_detailed_view(request, pk):
    cheque = get_object_or_404(WarehouseChequeModel, pk=pk)
    context = {
        "cheque": cheque,
        "details": cheque.cheque_items.all(),
    }
    return render(request, 'cheque/cheque_details.html', context)


@login_required
def cheque_item_count_update(request, pk, quantity):
    cheque_item = get_object_or_404(ChequeItemsModel, pk=pk)
    if not cheque_item.quantity == quantity:
        cheque_item.quantity = quantity
        cheque_item.modified_at = datetime.datetime.now()
        cheque_item.modified_by = request.user
        cheque_item.save(update_fields=["quantity", "modified_at", "modified_by"])
    return redirect("warehouse_v2:cheque-detailed", pk=cheque_item.cheque.pk)


@login_required
def add_item_to_cheque(request, ):
    data = json.loads(request.body)
    pk = data.get('id')
    quantity = data.get('quantity')
    cheque_pk = data.get('cheque')
    item = get_object_or_404(ItemsInStockModel, pk=pk)
    cheque = get_object_or_404(WarehouseChequeModel, pk=cheque_pk)
    ChequeItemsModel.objects.create(cheque=cheque, item=item, quantity=quantity, created_by=request.user,
                                    modified_by=request.user)
    return JsonResponse({}, status=200)


@login_required
def cheque_item_detailed_view(request, pk):
    context = {}
    cheque_item = get_object_or_404(ChequeItemsModel, pk=pk)
    if request.method == "GET":
        form = ChequeItemCountForm(instance=cheque_item)
        context["form"] = form
        context["item_name"] = cheque_item.item.item.name
        context["price"] = cheque_item.price
    elif request.method == "POST":
        form = ChequeItemCountForm(request.POST, instance=cheque_item)
        if form.is_valid():
            cheque_item: ChequeItemsModel = form.save(commit=False)
            cheque_item.modified_by = request.user
            cheque_item.modified_at = datetime.datetime.now()
            cheque_item.save()
            return redirect("warehouse_v2:cheque-detailed", pk=cheque_item.cheque.pk)
    return render(request, "cheque/cheque_item_update.html", context)


@csrf_exempt
def add_new_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.created_by = request.user
            patient.modified_by = request.user
            patient.save()
            return redirect('warehouse_v2:cheque-create')  # Replace with your success URL
    else:
        return redirect('warehouse_v2:cheque-create')
    return render(request, 'cheque/cheque_create.html', {'form': form})


def gen_invoice(request, pk):
    cheque = get_object_or_404(WarehouseChequeModel, pk=pk)
    context = {
        "cheque": cheque,
        "details": cheque.cheque_items.all(),
        "date": datetime.date.today()
    }
    return render(request, 'cheque/invoice.html', context)


def get_cheques_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        cheques = WarehouseChequeModel.objects.filter(
            Q(cheque_number__icontains=q)
        ).distinct()
        for new in cheques:
            queryset.append(new)

    return list(set(queryset))
