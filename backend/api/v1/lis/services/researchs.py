from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.v1.lis.serializers.labs import ListLabResearchSerializer, OrderedLabResearchSerializer, OrderedResearchPaginator
from api.v1.lis.serializers.orders import OrderedLabResearchFilterSerializer
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
        if request.user.branch:
            filters["branch_name__id"] = request.user.branch.id
        if data.get("start"):
            filters["created_at__date__gte"] = data.get("start")
        if data.get("end"):
            filters["created_at__date__lte"] = data.get("end")
        if data.get("barcode"):
            filters["barcode"] = data.get("barcode")
        if data.get("branch"):
            filters["branch_name__id"] = data.get("branch")
        if data.get("lab"):
            filters["lab__id"] = data.get("lab")
        if data.get("container"):
            filters["container_id"] = data.get("container")
        if data.get("category"):
            filters["lab__category__id"] = data.get("category")
        if data.get("patient"):
            filters["patient__id"] = data.get("patient")

        queryset = OrderedLabResearchModel.objects.filter(**filters)
        page = OrderedResearchPaginator.paginate_queryset(queryset, request)
        serializer_class = OrderedLabResearchSerializer(page, many=True)
        return Response(serializer_class.data)


def validate_ordered_research_service(request, pk):
    research = get_object_or_404(OrderedLabResearchModel, pk=pk)
    research.is_valid = True
    research.validated_by = request.user
    research.save(update_fields=["is_valid", "validated_by"])
    return Response({"message": "Success"}, status=200)
