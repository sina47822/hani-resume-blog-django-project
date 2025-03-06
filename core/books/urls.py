from django.urls import path
from .views import BooksListView,BooksDetailView,bookscategory,bookstags

namespaces = 'books'

urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),  # URL for books list
    path('<slug:slug>/', BooksDetailView.as_view(), name='books_detail'),
    path('category/<slug:slug>/',bookscategory , name='books_category'),
    path('tags/<slug:slug>/',bookstags , name='books_tags'),
    path('category/<slug:category_slug>/', BooksListView.as_view(), name='books_by_category'),
    path('tag/<slug:tag_slug>/', BooksListView.as_view(), name='books_by_tag'),
]