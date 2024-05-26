from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from api.v1.lis.serializers.orders import OrderedLabResearchSerializer, OrderedLabResearchFilterSerializer
from apps.lis.models import OrderedLabResearchModel, TestResultModel


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
            filters["created_at__date__gte"] = data.get("start")
        if data.get("end"):
            filters["created_at__date__lte"] = data.get("end")
        if data.get("barcode"):
            filters["barcode"] = data.get("barcode")
        if data.get("branch"):
            filters["branch_name__id"] = data.get("branch")
        queryset = OrderedLabResearchModel.objects.filter(**filters)
        serializer_class = OrderedLabResearchSerializer(queryset, many=True)
        return Response(serializer_class.data)


def update_test_container_code(request, pk):
    user = request.user
    test = get_object_or_404(TestResultModel, id=pk)
    container_code = request.data.get('container_code')
    if container_code and type(container_code) is str:
        test.container_code = container_code
        test.modified_by = user
        test.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
