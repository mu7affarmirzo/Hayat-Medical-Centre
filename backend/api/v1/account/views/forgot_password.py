# import random
#
# from drf_yasg.utils import swagger_auto_schema
# from passlib.handlers.pbkdf2 import pbkdf2_sha256
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
#
# from api.v1.account.serializers.otp import OtpSerializer, StepTwoSerializer, ForgotPasswordSerializer
# from api.v1.account.services.email import send_email
# from apps.account.models import Account
# from apps.account.models.otp import OtpModel
#
#
# @swagger_auto_schema(method="post", tags=["account"], request_body=OtpSerializer)
# @api_view(['POST'])
# def step_one(request):
#     if request.method == 'POST':
#
#         request_data = request.data
#         otp_code = str(random.randint(10000, 99999))
#         try:
#             send_email(request_data['email'], otp_code)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         enc_otp = pbkdf2_sha256.encrypt(otp_code, rounds=12000, salt_size=32)
#
#         serializer_data = {
#             'email': request_data['email'],
#             'otp': otp_code,
#             'enc_otp': enc_otp,
#         }
#
#         otp_code = OtpModel(email=request_data['email'])
#         serializer = OtpSerializer(otp_code, data=serializer_data)
#         data = {}
#
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'success': "Successfully sent and added",
#                 'otp_generated': enc_otp,
#             }
#             return Response(data=data, status=status.HTTP_201_CREATED)
#
#         return Response(data)
#
#
# @swagger_auto_schema(method="post", tags=["account"], request_body=StepTwoSerializer)
# @api_view(['POST'])
# def step_two(request):
#     if request.method == 'POST':
#         data = request.data
#         context = {}
#         try:
#             otp = OtpModel.objects.get(enc_otp=data['otp_token'])
#         except:
#             return Response({'status': False, 'message': 'This token has not been found.'})
#
#         if not otp.is_active:
#             return Response({'status': False, 'message': 'This token has been expired!'})
#
#         if pbkdf2_sha256.verify(data['otp'], otp.enc_otp):
#             try:
#                 user = Account.objects.get(email=otp.email)
#             except:
#                 return Response({'status': True, 'is_registered': False, 'message': 'This user should be registered!'})
#
#             refresh = RefreshToken.for_user(user)
#             context['jwt_token'] = {
#                 'status': True,
#                 'is_registered': True,
#                 'message': 'This user had been registered before',
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }
#             return Response(context)
#         else:
#             return Response({'status': False, 'message': 'The code is not correct'}, status=status.HTTP_404_NOT_FOUND)
#
#     return Response({'status': True, 'message': 'Code verified!'}, status=status.HTTP_200_OK)
#
#
# @swagger_auto_schema(method="put", tags=["account"], request_body=ForgotPasswordSerializer)
# @permission_classes((IsAuthenticated,))
# @api_view(['PUT'])
# def forgot_password(request):
#     try:
#         account = request.user
#     except Account.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'PUT':
#         serializer = ForgotPasswordSerializer(account, data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data['response'] = "Account password updated successfully!"
#             return Response(data=data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
