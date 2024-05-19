from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.v1.lis.serializers.labs import ListLabResearchSerializer
from apps.lis.models import LabResearchModel


def get_list_research_service(request, pk=None):
    if request.method == 'GET':
        queryset = LabResearchModel.objects.all()
        serializer_class = ListLabResearchSerializer(queryset, many=True)
        return Response(serializer_class.data)
