from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from OTP.models import OTPRequest
from . import serializers
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils import timezone
# Create your views here.
class OTPView(APIView):
    def get(self, request):
        serializer = serializers.RequestOTPSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                otp = OTPRequest.objects.generate(data)
                return Response(data=serializers.RequestOTPResponseSerializer(otp).data)
            except Exception as e:
                print (e)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data=serializer.errors)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    def post(self, request):
        serializer = serializers.RequestOTPSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                otp_request = OTPRequest.objects.generate(data)
                return Response(
                    data=serializers.RequestOTPResponseSerializer(otp_request).data,
                    status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        else:
            print(serializer.errors)  # چاپ خطاها برای بررسی
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def _handle_login(self, otp):
        User = get_user_model()

        query = User.objects.filter(email=otp['receiver'])

        if query.exists():
            created = False
            user = query.first()
        else:
            user = User.objects.create(email=otp['receiver'])
            created = True
        
        refresh = RefreshToken.for_user(user)

        return serializers.ObtainTokenSerializer({
            'refresh': str(refresh),
            'token': str(refresh.access_token),
            'created': created
        }).data
class VerifyOTPView(APIView):
    def post(self, request):
        serializer = serializers.VerifyOtpRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            print("Data received for OTP verification:", data)
            if OTPRequest.objects.is_valid(data['receiver'], data['request_id'], data['password']):
                return Response(self._handle_login(data))
            else:
                return Response({"error": "OTP نامعتبر است."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def _handle_login(self, otp_data):
        User = get_user_model()
        
        # جستجوی کاربر با استفاده از ایمیل یا شماره تلفن
        query = User.objects.filter(email=otp_data['receiver'])

        if query.exists():
            created = False
            user = query.first()
        else:
            user = User.objects.create(email=otp_data['receiver'])
            created = True

        refresh = RefreshToken.for_user(user)

        return serializers.ObtainTokenSerializer({
            'user_id': user.id,  # اضافه کردن شناسه کاربر
            'refresh': str(refresh),
            'token': str(refresh.access_token),
            'created': created
        }).data