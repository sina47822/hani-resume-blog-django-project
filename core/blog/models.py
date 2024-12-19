from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    )
    
    title = models.CharField(max_length=200)  # Title of the blog post
    summary = HTMLField(_('متن اول'),null = True, blank = True )
    content = HTMLField(_('متن اول'),null = True, blank = True )
    published_date = models.DateTimeField(auto_now_add=True)  # Automatically set when the blog is published
    updated_date = models.DateTimeField(auto_now=True)  # Automatically set when the blog is updated
    slug = models.SlugField(_('اسلاگ'),max_length = 250, null = True, blank = True , unique=True)

    def __str__(self):
        return self.title
    
    class Meta: 
        ordering = ('-published_date', ) 
        verbose_name = _('مقالات')
        verbose_name_plural = verbose_name