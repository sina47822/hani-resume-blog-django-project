from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post

# Blog List View
class BlogListView(View):
    template_name = "blog/blog_list.html"
    
    def get(self, request):
        # Query all blog posts
        blogs = Post.objects.all()
        context = {
            'blogs': blogs,
        }
        return render(request, self.template_name, context)

# Blog Detail View
class BlogDetailView(View):
    template_name = "blog/blog_detail.html"
    
    def get(self, request, pk):
        # Retrieve the blog post by primary key (pk)
        blog = get_object_or_404(Post, pk=pk)
        context = {
            'blog': blog,
        }
        return render(request, self.template_name, context)