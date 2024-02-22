from django.db.models import Q, Count
from django.forms import model_to_dict
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.sanatorium.serializers import *
from apps.sanatorium.models import *


@swagger_auto_schema(tags=['sanatorium'], method="get", )
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def ib_by_id_doctors_view(request, pk):

    context = {
        "documents": {},
        "regime": "",
        "highlighted_tags": {
            "allergy": False,
            "meteolabel": False,
            "food_issues": False,
            "furniture_fault": False,
            "pills_drugs": False
        }
    }
    ill_his = get_object_or_404(IllnessHistory, pk=pk)
    serializer = DoctorsIllnessHistorySerializer(ill_his)

    return Response({**serializer.data, **context})
