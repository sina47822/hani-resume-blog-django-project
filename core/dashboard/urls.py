from django.urls import path,include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("home/",views.DashboardHomeView.as_view(),name="home"),
    
    # include admin urls
    path("hamgam/",include('dashboard.hamgam.urls')),
    
    # include customer urls
    path("hamrah/",include('dashboard.hamrah.urls')),
]