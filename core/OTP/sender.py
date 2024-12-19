from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail

# Create your views here.
def send_otp(request):
    from .models import OTPRequest
    if request.method == "POST":
        receiver = request.POST.get("receiver")  # ایمیل یا شماره تماس
        channel = request.POST.get("channel", OTPRequest.OtpChannel.EMAIL)  # پیش‌فرض ایمیل

        if not receiver:
            return JsonResponse({"error": "گیرنده لازم است."}, status=400)

        if channel not in OTPRequest.OtpChannel.values:
            return JsonResponse({"error": "کانال نامعتبر است."}, status=400)

        otp_request = OTPRequest.objects.generate({"channel": channel, "receiver": receiver})
        
        return JsonResponse({
            "message": "کد OTP ارسال شد.",
            "request_id": str(otp_request.request_id),  # ارسال request_id برای تأیید بعدی
        })
    return JsonResponse({"error": "فقط درخواست‌های POST پشتیبانی می‌شوند."}, status=405)
def send_otp(otp_request):
    if otp_request.channel == otp_request.OtpChannel.EMAIL:
        try:
            send_mail(
                "کد تأیید شما",
                f"کد تأیید شما: {otp_request.password}",
                "your-email@example.com",
                [otp_request.receiver],
                fail_silently=False,
            )
        except Exception as e:
            # ثبت خطا در لاگ
            print(f"خطا در ارسال ایمیل: {e}")
            raise e
    elif otp_request.channel == otp_request.OtpChannel.PHONE:
        # ارسال پیامک (باید از یک سرویس ارسال پیامک استفاده کنید)
        print(f"ارسال پیامک به {otp_request.receiver} با کد: {otp_request.password}")