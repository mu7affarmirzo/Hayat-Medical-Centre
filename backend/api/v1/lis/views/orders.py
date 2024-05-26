from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from api.v1.lis.serializers.orders import OrderedLabResearchSerializer, OrderedLabResearchFilterSerializer, \
    UpdateContainerCodeSerializer
from api.v1.lis.services.orders import get_list_ordered_researches_service, update_test_container_code
from apps.lis.models import OrderedLabResearchModel


@swagger_auto_schema(tags=['lis'], method="get", query_serializer=OrderedLabResearchFilterSerializer)
@api_view(['get', ])
@permission_classes((IsAuthenticated,))
def get_list_ordered_researches(request, pk=None):
    response = get_list_ordered_researches_service(request, pk=pk)
    return response


@swagger_auto_schema(tags=['lis'], method="post", request_body=UpdateContainerCodeSerializer)
@api_view(['post', ])
@permission_classes((IsAuthenticated,))
def update_test_container_code_view(request, pk):
    response = update_test_container_code(request, pk=pk)
    return response
