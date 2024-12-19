from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save
from account.validators import validate_iranian_cellphone_number

class UserType(models.IntegerChoices):
    hamgam = 1, _("hamgam")
    hamrah = 2, _("hamrah")
    admin = 3, _("admin")

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, phone_number=None, password=None, **extra_fields):
        """
        Create and save a User with the given phone number and password.
        """

        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, phone_number=None, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("type", UserType.admin.value)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=200,blank=True) 
    last_name = models.CharField(max_length=200,blank=True) 
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex],max_length=200,blank=True,null=True) 
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)
    type = models.IntegerField(
        choices=UserType.choices, default=UserType.hamgam.value)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email" # Use email for Authentication
    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE,related_name="user_profile")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = HTMLField(_('زندگی نامه'),null = True, blank = True )
    # work = 
    # interest = 
    avatar = models.ImageField(upload_to="profile/",default="profile/default.png")
    phone_number = models.CharField(max_length=12, validators=[validate_iranian_cellphone_number])

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def get_fullname(self):
        if self.first_name or self.last_name:
            return self.first_name + " " + self.last_name
        return "کاربر جدید"

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance, pk=instance.pk)