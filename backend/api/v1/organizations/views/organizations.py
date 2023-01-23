from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.account.models import OrganizationModel, BranchModel
from rest_framework.generics import CreateAPIView, ListCreateAPIView

from api.v1.organizations.serializers.organizations import OrganizationCreateSerializer, OrganizationListSerializer, \
    BranchListSerializer, BranchCreateSerializer


class OrganizationsListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['organizations'])
    def get(self, request, format=None):
        organizations = OrganizationModel.objects.all()
        serializer = OrganizationListSerializer(organizations, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['organizations'], request_body=OrganizationCreateSerializer)
    def post(self, request, format=None):
        account = request.user
        organizations = OrganizationModel(created_by=account, modified_by=account)
        serializer = OrganizationCreateSerializer(organizations, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchesListCreateView(APIView):

    @swagger_auto_schema(tags=['organizations'])
    def get(self, request, format=None):
        branches = BranchModel.objects.all()
        serializer = BranchListSerializer(branches, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['organizations'], request_body=BranchCreateSerializer)
    @permission_classes((IsAuthenticated,))
    def post(self, request, format=None):
        account = request.user
        branch = BranchModel(created_by=account, modified_by=account)
        serializer = BranchCreateSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
