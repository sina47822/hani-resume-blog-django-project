from django.contrib import admin
from .models import Books,Tags,Category

admin.site.register(Books)
admin.site.register(Tags)
admin.site.register(Category)