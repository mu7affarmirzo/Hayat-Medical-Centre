from django.db.models import Q, Count
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
        "patient": {},
        "documents": {},
        "ib_history": {},
        "booking": {},
        "factors": [],
        "tags": "",
        "regime": "",
        "first_diagnosis": "",
        "arrival_diagnosis": "",
        "actual_diagnosis": "",
        "risk_factors": [],
        "highlighted_tags": {
            "allergy": False,
            "meteolabel": False,
            "Food issues": False,
            "Furniture fault": False,
            "Pills Drugs": False
        }
    }
    ill_his = get_object_or_404(IllnessHistory, pk=pk)

    return Response(context)
