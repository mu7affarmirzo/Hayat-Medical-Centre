from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models.accounts import Account


class DoctorsListCreateView(APIView):

    @swagger_auto_schema(tags=['organizations'])
    def post(self, request, format=None):
        branches = Account.objects.all()
        serializer = BranchListSerializer(branches, many=True)
        return Response(serializer.data)

