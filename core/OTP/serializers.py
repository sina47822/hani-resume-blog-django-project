from rest_framework import serializers
from OTP.models import OTPRequest

class RequestOTPSerializer(serializers.Serializer):
    receiver = serializers.EmailField(required=True, help_text="ایمیل یا شماره تلفن گیرنده")
    channel = serializers.ChoiceField(
        choices=OTPRequest.OtpChannel.choices,
        default=OTPRequest.OtpChannel.EMAIL,
        help_text="کانال ارسال OTP (ایمیل یا پیامک)"
    )

class RequestOTPResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTPRequest
        fields = ['request_id', 'receiver', 'channel', 'created']

class VerifyOtpRequestSerializer(serializers.Serializer):
    receiver = serializers.EmailField(required=True, help_text="ایمیل گیرنده کد OTP")
    request_id = serializers.UUIDField(required=True, help_text="شناسه درخواست OTP")
    password = serializers.CharField(max_length=6, required=True, help_text="کد OTP")

class ObtainTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField(help_text="توکن Refresh برای احراز هویت")
    token = serializers.CharField(help_text="توکن دسترسی (Access Token)")
    created = serializers.BooleanField(help_text="آیا کاربر جدید ایجاد شده است؟")