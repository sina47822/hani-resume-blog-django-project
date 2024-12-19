from django.http import HttpResponse
from django.views.generic import View, TemplateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasHamgamAccessPermission
from django.contrib.auth import views as auth_views
from dashboard.hamgam.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from account.models import Profile
from django.shortcuts import redirect
from django.contrib import messages


class CustomerSecurityEditView(LoginRequiredMixin, HasHamgamAccessPermission,SuccessMessageMixin, auth_views.PasswordChangeView):
    template_name = "dashboard/hamgam/profile/security-edit.html"
    form_class = CustomerPasswordChangeForm
    success_url = reverse_lazy("dashboard:hamgam:security-edit")
    success_message = "بروز رسانی پسورد با موفقیت انجام شد"


class CustomerProfileEditView(LoginRequiredMixin, HasHamgamAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/hamgam/profile/profile-edit.html"
    form_class = CustomerProfileEditForm
    success_url = reverse_lazy("dashboard:hamgam:profile-edit")
    success_message = "بروز رسانی پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

class CustomerProfileImageEditView(LoginRequiredMixin, HasHamgamAccessPermission,SuccessMessageMixin,UpdateView):
    http_method_names=["post"]
    model = Profile
    fields= [
        "image"
    ]
    success_url = reverse_lazy("dashboard:hamgam:profile-edit")
    success_message = "بروز رسانی تصویر پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    
    def form_invalid(self, form):
        messages.error(self.request,"ارسال تصویر با مشکل مواجه شده لطف مجدد بررسی و تلاش نمایید")
        return redirect(self.success_url)