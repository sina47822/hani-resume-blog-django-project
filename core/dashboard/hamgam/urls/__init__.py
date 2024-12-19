from django.urls import path,include

app_name = "hamgam"

urlpatterns = [
    path("",include("dashboard.hamgam.urls.generals")),
    path("",include("dashboard.hamgam.urls.profiles")),
]