from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),  # URL for blog list
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),  # URL for blog detail
]
