from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from account.models import User
from django.contrib.auth import get_user_model

# fetching user model
User = get_user_model()

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    )
    author = models.ForeignKey(User , on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)  # Title of the blog post
    summary = HTMLField(_('خلاصه'),null = True, blank = True )
    content = HTMLField(_('متن'),null = True, blank = True )
    published_date = models.DateTimeField(auto_now_add=True)  # Automatically set when the blog is published
    updated_date = models.DateTimeField(auto_now=True)  # Automatically set when the blog is updated
    slug = models.SlugField(_('اسلاگ'),max_length = 250, null = True, blank = True , unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    tags = models.ManyToManyField('Tags')
    status = models.CharField(max_length=100 , choices=STATUS_CHOICES, default='Draft',blank = True, null = True)
    thumbnail = models.ImageField( upload_to= 'posts/thumbnails/%Y/%m' , default='posts/thumbnails/squre_images/1.jpg')
    total_views = models.IntegerField(default=0)
    class Meta: 
        ordering = ('-published_date', )
        
    def __str__(self):
        return self.title
    
    class Meta: 
        ordering = ('-published_date', ) 
        verbose_name = _('قلم من')
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:blog-detail',
                        kwargs={'slug': self.slug})
    
class Category(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    slug = models.SlugField(_('اسلاگ'),max_length = 50, null = True, blank = True , unique=True)
    parent = models.ForeignKey('self' , on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog:blog-category', kwargs={'slug': self.slug})

class Tags(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    slug = models.SlugField(_('اسلاگ'),max_length = 50, null = True, blank = True , unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog-tags', kwargs={'slug': self.slug})
    
class PostSEO(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='seo_images/', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='post')
    def __str__(self):
        return self.title
    
class TagsSEO(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='seo_images/', null=True, blank=True)
    tags_seo = models.ForeignKey(Tags, on_delete=models.CASCADE, blank=True, null=True, related_name='posttags')
    def __str__(self):
        return self.title
    
class CategorySEO(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='seo_images/', null=True, blank=True)
    Category_seo = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='postcategory')
    def __str__(self):
        return self.title