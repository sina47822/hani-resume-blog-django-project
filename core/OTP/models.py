from django.db import models
from django.utils.timezone import now
import random
from datetime import timedelta
from django.utils import timezone
import uuid

class OtpRequstQuerySet(models.QuerySet):
    def is_valid(self, receiver, request_id, password):
        current_time = timezone.now()
        return self.filter(
            receiver=receiver,
            request_id=request_id,
            password=password,
            created__lt=current_time,
            created__gt=current_time - timedelta(seconds=300)
        ).exists()

class OTPManager(models.Manager):
    
    def get_queryset(self):
        return OtpRequstQuerySet(self.model, self._db)
    
    def is_valid(self, receiver, request, password):
        return self.get_queryset().is_valid(receiver, request, password)

    def generate(self, data):
        from .sender import send_otp
        print(f"Data received for OTP generation: {data}")  # اضافه کردن لاگ
        current_time = timezone.now()
        # Check if an unexpired OTP already exists for the receiver
        existing_otp = self.filter(
            receiver=data['receiver'],
            created__gt=current_time - timedelta(seconds=120)  # OTP valid for 120 seconds
        ).first()
        print(f"Existing OTP: {existing_otp}")

        if existing_otp:
            # If an existing OTP is still valid, return the same one
            return existing_otp
        
        # Otherwise, create a new OTP request
        otp = self.model(channel=data['channel'], receiver=data['receiver'])
        otp.save(using=self._db)
        send_otp(otp)  # Send OTP to the user
        return otp

def generate_otp():
    return f"{random.randint(100000, 999999)}"
            
class OTPRequest(models.Model):
    class OtpChannel(models.TextChoices):
        PHONE = 'phone'
        EMAIL = 'email'

    request_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    channel = models.CharField(max_length=10, choices=OtpChannel.choices, default=OtpChannel.EMAIL)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    is_verified = models.BooleanField(default=False)
    receiver = models.CharField(max_length=50)
    password = models.CharField(max_length=6, default=generate_otp)

    objects = OTPManager()