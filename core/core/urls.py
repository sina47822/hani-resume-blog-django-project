"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler400,handler403, handler404, handler500

from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.i18n import set_language

from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('tarjome', include('rosetta.urls')),

    path('', include(('website.urls' , 'website'), namespace= 'website')),
    path('posts/', include(('blog.urls' , 'blog'), namespace= 'blog')),
    path('books/', include(('books.urls' , 'books'), namespace= 'books')),
    path('', include('website.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('account.urls')),
    path('comment/', include('comment.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/', include('OTP.urls')),
    
    path('tinymce/', include('tinymce.urls')),
    path('robots.txt', include('robots.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]
handler400 = 'website.views.handler_400'
handler403 = 'website.views.handler_403'
handler404 = 'website.views.handler_404'
handler500 = 'website.views.handler_500'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)