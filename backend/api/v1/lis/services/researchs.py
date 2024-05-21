from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.v1.lis.serializers.labs import ListLabResearchSerializer, OrderedLabResearchSerializer, \
    OrderedLabResearchFilterSerializer
from apps.lis.models import LabResearchModel, OrderedLabResearchModel


def get_list_research_service(request, pk=None):
    if request.method == 'GET':
        queryset = LabResearchModel.objects.all()
        serializer_class = ListLabResearchSerializer(queryset, many=True)
        return Response(serializer_class.data)


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