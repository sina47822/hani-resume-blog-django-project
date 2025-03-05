from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from django.views import View
from .models import Books,Category,Tags,CategorySEO,TagsSEO,BooksSEO

def bookscategory(request, slug):
    category = get_object_or_404(Category, slug=slug)  # Retrieve the category object based on the slug
    books = Books.objects.filter(category=category)  # Filter books based on the category object

    seo = CategorySEO.objects.filter(Category_seo=category).first()

    paginator = Paginator(books, 8)  # Show 10 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    context = {'category': category, 'page_obj': page_obj, 'seo': seo, 'books' : books}

    return render(request, 'books/category.html', context)

def bookstags(request, slug):
    tag = get_object_or_404(Tags, slug=slug)  # Retrieve the category object based on the slug
    books = Books.objects.filter(tags=tag)  # Filter books based on the category object
    seo = TagsSEO.objects.filter(tags_seo=tag).first()

    paginator = Paginator(books, 8)  # Show 10 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'tag': tag,'page_obj' :page_obj , 'books': books, 'seo' : seo}
    return render(request, 'books/tags.html', context)

# books List View
class BooksListView(View):
    template_name = "books/books_list.html"
    
    def get(self, request):
        # Query all books books
        books = Books.objects.all()
        categories = Category.objects.all()
        tags = Tags.objects.all()

        paginator = Paginator(books, 4)  # Show 10 books per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        latests = Books.objects.all().order_by('published_date')[:5]  # Example: fetching the 1 latest books

        context = {
            'books': books,
            'latests': latests,
            'categories': categories,
            'tags': tags,
            'page_obj': page_obj,
        }
        return render(request, self.template_name, context)

# books Detail View
class BooksDetailView(View):
    template_name = "books/books_detail.html"
    
    def get(self, request, slug):
        # Retrieve the books books by primary key (pk)
        books = get_object_or_404(Books, slug =slug )
        seo = BooksSEO.objects.filter(books=books).first()  # Retrieve the first BooksSEO object associated with the books
        books_related = Books.objects.all().order_by('-id')[:4]
        categories = Category.objects.all()
        tags = Tags.objects.all()

        context = { 'slug': slug,
                    'books' : books,
                    'seo' : seo,
                    'books_related': books_related,
                    'categories':categories,
                    'tags' : tags
                }

        return render(request, self.template_name, context)