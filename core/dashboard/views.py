from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from account.models import UserType


class DashboardHomeView(LoginRequiredMixin,View):
    
    def dispatch(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            if request.user.type == UserType.hamgam.value:
                return redirect(reverse_lazy('dashboard:hamgam:home'))
            if request.user.type == UserType.hamrah.value:
                return redirect(reverse_lazy('dashboard:hamrah:home'))
        else:
            return redirect(reverse_lazy('account:login'))
        return super().dispatch(request, *args, **kwargs)