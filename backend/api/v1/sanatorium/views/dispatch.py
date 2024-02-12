from django.db.models import Q, Count
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.sanatorium.services import dispatch


@swagger_auto_schema(tags=['sanatorium'], method="get", )
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def get_patients(request):
    response = dispatch.get_patients(request)
    return Response(response)


@swagger_auto_schema(tags=['sanatorium'], method="get", )
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def get_patients(request):
    response = dispatch.get_patients(request)
    return Response(response)
