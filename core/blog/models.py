from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    summary = models.TextField()  # A brief summary of the blog post
    content = models.TextField()  # Full content of the blog post
    published_date = models.DateTimeField(auto_now_add=True)  # Automatically set when the blog is published
    updated_date = models.DateTimeField(auto_now=True)  # Automatically set when the blog is updated

    def __str__(self):
        return self.title