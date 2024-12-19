from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from OTP.models import OTPRequest
from . import serializers
from django.contrib.auth import get_user_model

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
        serializer = serializers.VerifyOtpRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if OTPRequest.objects.is_valid(data['receiver'],data['request_id'], data['password']):
                return Response(self._handle_login(data))
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
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
def verify_otp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        otp = request.POST.get("otp")

        try:
            otp_request = OTPRequest.objects.get(email=email, otp=otp)
        except OTPRequest.DoesNotExist:
            return JsonResponse({"error": "ایمیل یا کد OTP نامعتبر است."}, status=400)

        if otp_request.is_verified:
            return JsonResponse({"error": "کد OTP قبلاً تأیید شده است."}, status=400)

        if otp_request.is_expired():
            return JsonResponse({"error": "کد OTP منقضی شده است."}, status=400)

        otp_request.is_verified = True
        otp_request.save()
        return JsonResponse({"message": "کد OTP با موفقیت تأیید شد!"})