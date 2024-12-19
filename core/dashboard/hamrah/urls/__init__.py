from django.urls import path,include

app_name = "hamrah"

urlpatterns = [
    path("",include("dashboard.hamrah.urls.generals")),
    path("",include("dashboard.hamrah.urls.profiles")),
    path("",include("dashboard.hamrah.urls.reviews")),
    path("",include("dashboard.hamrah.urls.newsletters")),
    path("",include("dashboard.hamrah.urls.contacts")),
    path("",include("dashboard.hamrah.urls.users")),
]