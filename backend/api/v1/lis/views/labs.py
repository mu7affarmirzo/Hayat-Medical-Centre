# views.py
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from apps.lis.models.lab_researchs import LabResearchCategoryModel
from ..serializers.labs import LabResearchCategorySerializer, ListCategorySerializer
from ..services.researchs import get_list_research_service


class LabResearchCategoryListAPIView(generics.ListAPIView):
    queryset = LabResearchCategoryModel.objects.all()
    serializer_class = LabResearchCategorySerializer


class ListResearchCategoryListAPIView(generics.ListAPIView):
    queryset = LabResearchCategoryModel.objects.all()
    serializer_class = ListCategorySerializer


@swagger_auto_schema(tags=['lis'], method="get")
@api_view(['get', ])
@permission_classes((IsAuthenticated,))
def get_list_research(request):
    response = get_list_research_service(request)
    return response

