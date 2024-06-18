from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.v1.lis.serializers.orders import OrderedLabResearchSerializer, OrderedLabResearchFilterSerializer, \
    UpdateContainerCodeSerializer
from apps.lis.models import OrderedLabResearchModel, TestResultModel


class ResearchesPaginator(PageNumberPagination):
    page_size = 10


def get_list_ordered_researches_service(request, pk=None):
    if request.method == 'GET':
        if pk:
            obj = get_object_or_404(OrderedLabResearchModel, pk=pk)
            serializer_class = OrderedLabResearchSerializer(obj)
            return Response([serializer_class.data])

        filters = {}
        serializer = OrderedLabResearchFilterSerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
        if data.get("start"):
            filters["created_at__date__lte"] = data.get("start")
        if data.get("end"):
            filters["created_at__date__gte"] = data.get("end")
        if data.get("barcode"):
            filters["lab_code"] = data.get("barcode")
        if data.get("lab"):
            filters["lab__id"] = data.get("lab")
        if data.get("container"):
            filters["container_id"] = data.get("container")
        if data.get("branch"):
            filters["branch_name__id"] = data.get("branch")
        if data.get("category"):
            filters["lab__category__id"] = data.get("category")
        if data.get("patient"):
            filters["patient__id"] = data.get("patient")
        if data.get("order_status"):
            filters["order_status"] = data.get("oder_status")
        queryset = OrderedLabResearchModel.objects.filter(**filters)
        paginator = ResearchesPaginator()
        paginated_page = paginator.paginate_queryset(queryset, request)
        serializer_class = OrderedLabResearchSerializer(paginated_page, many=True)
        return paginator.get_paginated_response(serializer_class.data)


def update_test_container_code(request, pk):
    user = request.user
    test = get_object_or_404(TestResultModel, id=pk)
    container_data = UpdateContainerCodeSerializer(data=request.data)
    if container_data.is_valid(raise_exception=True):
        container_code = container_data.data.get('container_code')

        #  TODO: add container id update
        container_id = container_data.data.get('container_id')
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if container_code and type(container_code) is str:
        test.container_code = container_code
        test.modified_by = user
        test.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
