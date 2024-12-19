from django.urls import path
from .views import BlogListView, BlogDetailView,postcategory,posttags

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),  # URL for blog list
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('category/<slug:slug>/',postcategory , name='blog-category'),
    path('tags/<slug:slug>/',posttags , name='blog-tags'),
]
