from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from django.views import View
from .models import Post,Category,Tags,CategorySEO,TagsSEO,PostSEO

def postcategory(request, slug):
    category = get_object_or_404(Category, slug=slug)  # Retrieve the category object based on the slug
    posts = Post.objects.filter(categories=category)  # Filter posts based on the category object

    seo = CategorySEO.objects.filter(Category_seo=category).first()

    paginator = Paginator(posts, 8)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    context = {'category': category, 'page_obj': page_obj, 'seo': seo, 'posts' : posts}

    return render(request, 'blog/category.html', context)

def posttags(request, slug):
    tag = get_object_or_404(Tags, slug=slug)  # Retrieve the category object based on the slug
    posts = Post.objects.filter(tags=tag)  # Filter posts based on the category object
    seo = TagsSEO.objects.filter(tags_seo=tag).first()

    paginator = Paginator(posts, 8)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'tag': tag,'page_obj' :page_obj , 'posts': posts, 'seo' : seo}
    return render(request, 'blog/tags.html', context)

# Blog List View
class BlogListView(View):
    template_name = "blog/blog_list.html"
    
    def get(self, request):
        # Query all blog posts
        blogs = Post.objects.all()
        categories = Category.objects.all()
        tags = Tags.objects.all()

        paginator = Paginator(blogs, 4)  # Show 10 posts per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        latests = Post.objects.all().order_by('published_date')[:5]  # Example: fetching the 1 latest posts

        context = {
            'blogs': blogs,
            'latests': latests,
            'categories': categories,
            'tags': tags,
            'page_obj': page_obj,
        }
        return render(request, self.template_name, context)

# Blog Detail View
class BlogDetailView(View):
    template_name = "blog/blog_detail.html"
    
    def get(self, request, slug):
        # Retrieve the blog post by primary key (pk)
        post = get_object_or_404(Post, slug =slug )
        seo = PostSEO.objects.filter(post=post).first()  # Retrieve the first PostSEO object associated with the post
        posts = Post.objects.all().order_by('-id')[:4]
        categories = Category.objects.all()
        tags = Tags.objects.all()

        context = { 'slug': slug,
                    'post' : post,
                    'seo' : seo,
                    'posts': posts,
                    'categories':categories,
                    'tags' : tags
                }

        return render(request, self.template_name, context)