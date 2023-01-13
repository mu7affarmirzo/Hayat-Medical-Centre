from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from api.v1.cashbox.servives.transaction_service import payment_proceed_service
from apps.cashbox.models import TransactionsModel
from api.v1.appointment.serializers.appointment import TimeSerializer
from django.shortcuts import get_object_or_404
from api.v1.cashbox.serializers import TransactionsSerializer, CreateTransactionSerializer, TransactionsListSerializer, TypeSerializer


class TransactionsView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['transactions'])
    def get(self, request, format=None):
        # start_date = self.request.query_params.get("start_date", datetime.today().date())
        # end_date = self.request.query_params.get("end_date", datetime.today().date())
        # transactions = TransactionsModel.objects.filter(created_at__range=(start_date, end_date))
        transactions = TransactionsModel.objects.filter(duty__is_closed=False, created_by=request.user)
        serializer = TransactionsSerializer(transactions, many=True)
        # serializer = TransactionsListSerializer(transactions, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['payment'], request_body=CreateTransactionSerializer)
    def post(self, request, format=None):
        response = payment_proceed_service(request)
        return response


class RetrieveTransactionsView(RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = TransactionsSerializer
    queryset = TransactionsModel

    @swagger_auto_schema(tags=['transactions'])
    def get(self, request, pk, format=None):
        transactions = get_object_or_404(TransactionsModel, appointment_id=pk)
        serializer = TransactionsSerializer(transactions)
        return Response(serializer.data)

    @swagger_auto_schema(tags=['transactions'])
    def delete(self, request, pk, format=None):
        transactions = get_object_or_404(TransactionsModel, appointment_id=pk)
        transactions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', tags=['transactions'])
@permission_classes((IsAuthenticated,))
@api_view(['GET', ])
def get_by_tr_id_view(request, pk):
    transactions = get_object_or_404(TransactionsModel, id=pk)
    serializer = TransactionsSerializer(transactions)
    return Response(serializer.data)


@swagger_auto_schema(method='get', tags=['transactions'])
@permission_classes((IsAuthenticated,))
@api_view(['GET', ])
def get_by_duty_id_view(request, pk):
    transactions = get_object_or_404(TransactionsModel, duty_id=pk)
    serializer = TransactionsSerializer(transactions)
    return Response(serializer.data)


@swagger_auto_schema(method="post", tags=["transactions"], request_body=TimeSerializer, manual_parameters=[
            openapi.Parameter('min', openapi.IN_QUERY,
                      type='date'),
            openapi.Parameter('max', openapi.IN_QUERY,
                      type='date'),
        ],)
@permission_classes((IsAuthenticated,))
@api_view(['POST', ])
def transactions_time_view(request):
    min_date = request.data['min']
    max_date = request.data['max']
    transactions = TransactionsModel.objects.filter(created_at__range=[min_date, max_date])
    serializer = TransactionsSerializer(transactions, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method="post", tags=["transactions"], request_body=TypeSerializer)
@permission_classes((IsAuthenticated,))
@api_view(['POST', ])
def transactions_type_filter(request):
    type = request.data['type']
    transactions = TransactionsModel.objects.filter(transaction_type=type)
    serializer = TransactionsSerializer(transactions, many=True)
    return Response(serializer.data)

