from rest_framework import serializers
from OTP.models import OTPRequest

class RequestOTPSerializer(serializers.Serializer):
    receiver = serializers.CharField(required=True, help_text="ایمیل گیرنده یا شماره تماس")
    channel = serializers.ChoiceField(choices=OTPRequest.OtpChannel.choices, default=OTPRequest.OtpChannel.EMAIL)

    def validate_receiver(self, value):
        if self.initial_data.get('channel') == OTPRequest.OtpChannel.EMAIL:
            # Validate email
            from django.core.validators import validate_email
            try:
                validate_email(value)
            except Exception:
                raise serializers.ValidationError("ایمیل نامعتبر است.")
        else:
            # Validate phone number (basic check)
            if not value.isdigit():
                raise serializers.ValidationError("شماره تماس نامعتبر است.")
        return value

class RequestOTPResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTPRequest
        fields = ['request_id', 'receiver', 'channel', 'created', 'password']  # اضافه کردن فیلد password
        
class VerifyOtpRequestSerializer(serializers.Serializer):
    receiver = serializers.EmailField(required=True, help_text="ایمیل گیرنده کد OTP")
    request_id = serializers.UUIDField(required=True, help_text="شناسه درخواست OTP")
    password = serializers.CharField(max_length=6, required=True, help_text="کد OTP")

class ObtainTokenSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(help_text="شناسه کاربر")
    refresh = serializers.CharField(help_text="توکن Refresh برای احراز هویت")
    token = serializers.CharField(help_text="توکن دسترسی (Access Token)")
    created = serializers.BooleanField(help_text="آیا کاربر جدید ایجاد شده است؟")