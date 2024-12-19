from django.views.generic import View, TemplateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasHamrahAccessPermission
from django.contrib.auth import views as auth_views
from dashboard.hamrah.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from account.models import Profile
from django.shortcuts import redirect
from django.contrib import messages


class AdminSecurityEditView(LoginRequiredMixin, HasHamrahAccessPermission,SuccessMessageMixin, auth_views.PasswordChangeView):
    template_name = "dashboard/hamrah/profile/security-edit.html"
    form_class = AdminPasswordChangeForm
    success_url = reverse_lazy("dashboard:hamrah:security-edit")
    success_message = "بروز رسانی پسورد با موفقیت انجام شد"


class AdminProfileEditView(LoginRequiredMixin, HasHamrahAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = "dashboard/hamrah/profile/profile-edit.html"
    form_class = AdminProfileEditForm
    success_url = reverse_lazy("dashboard:hamrah:profile-edit")
    success_message = "بروز رسانی پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

class AdminProfileImageEditView(LoginRequiredMixin, HasHamrahAccessPermission,SuccessMessageMixin,UpdateView):
    http_method_names=["post"]
    model = Profile
    fields= [
        "image"
    ]
    success_url = reverse_lazy("dashboard:hamrah:profile-edit")
    success_message = "بروز رسانی تصویر پروفایل با موفقیت انجام شد"
    
    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    
    def form_invalid(self, form):
        messages.error(self.request,"ارسال تصویر با مشکل مواجه شده لطف مجدد بررسی و تلاش نمایید")
        return redirect(self.success_url)