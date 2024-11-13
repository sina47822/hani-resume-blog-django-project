from django.contrib import sitemaps
from django.urls import reverse

from django.contrib.sitemaps import Sitemap

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ['website:index', 'website:about', 'website:contact', 'website:resume']
    
    def location(self, obj):
        return reverse(obj)