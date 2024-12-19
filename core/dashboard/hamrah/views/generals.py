from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasHamrahAccessPermission


class AdminDashboardHomeView(LoginRequiredMixin, HasHamrahAccessPermission, TemplateView):
    template_name = "dashboard/admin/home.html"