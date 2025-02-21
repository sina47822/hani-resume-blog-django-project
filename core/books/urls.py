from django.urls import path
from .views import BooksListView,BooksDetailView,bookscategory,bookstags

namespaces = 'books'

urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),  # URL for books list
    path('<slug:slug>/', BooksDetailView.as_view(), name='books_detail'),
    path('category/<slug:slug>/',bookscategory , name='books-category'),
    path('tags/<slug:slug>/',bookstags , name='books-tags'),
]