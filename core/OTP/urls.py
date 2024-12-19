from django.urls import path
from .views import OTPView,VerifyOTPView


urlpatterns = [
    path('otp/', OTPView.as_view(), name='otp_view'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
]