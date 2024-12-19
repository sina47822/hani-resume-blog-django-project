from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import OTPRequest

def send_otp(request):
    if request.method == "POST":
        receiver = request.POST.get("receiver")
        channel = request.POST.get("channel", OTPRequest.OtpChannel.EMAIL)  # Default to email

        if not receiver:
            return JsonResponse({"error": "گیرنده لازم است."}, status=400)

        if channel not in dict(OTPRequest.OtpChannel.choices).keys():
            return JsonResponse({"error": "کانال نامعتبر است."}, status=400)

        try:
            otp_request = OTPRequest.objects.generate({"channel": channel, "receiver": receiver})
            send_otp_message(otp_request)
        except Exception as e:
            return JsonResponse({"error": f"خطا در ارسال OTP: {str(e)}"}, status=500)

        return JsonResponse({
            "message": "کد OTP ارسال شد.",
            "request_id": str(otp_request.request_id),
        })

    return JsonResponse({"error": "فقط درخواست‌های POST پشتیبانی می‌شوند."}, status=405)
import logging

logger = logging.getLogger(__name__)
def send_otp_message(otp_request):
    try:
        if otp_request.channel == OTPRequest.OtpChannel.EMAIL:
            send_mail(
                "کد تأیید شما",
                f"کد تأیید شما: {otp_request.password}",
                "no-reply@example.com",
                [otp_request.receiver],
            )
        elif otp_request.channel == OTPRequest.OtpChannel.PHONE:
            logger.info(f"ارسال پیامک به {otp_request.receiver} با کد: {otp_request.password}")
        else:
            raise ValueError("کانال ارسال نامعتبر است.")
    except Exception as e:
        logger.error(f"خطا در ارسال OTP: {e}")
        raise e