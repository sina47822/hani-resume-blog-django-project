from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasHamgamAccessPermission


class CustomerDashboardHomeView(LoginRequiredMixin, HasHamgamAccessPermission, TemplateView):
    template_name = "dashboard/hamgam/home.html"