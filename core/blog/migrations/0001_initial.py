# Generated by Django 5.1.3 on 2025-01-30 09:39

import django.db.models.deletion
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='اسلاگ')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='اسلاگ')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.category')),
            ],
        ),
        migrations.CreateModel(
            name='CategorySEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('Category_seo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postcategory', to='blog.category')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', tinymce.models.HTMLField(blank=True, null=True, verbose_name='خلاصه')),
                ('content', tinymce.models.HTMLField(blank=True, null=True, verbose_name='متن')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True, verbose_name='اسلاگ')),
                ('status', models.CharField(blank=True, choices=[('draft', 'Draft'), ('published', 'Published')], default='Draft', max_length=100, null=True)),
                ('thumbnail', models.ImageField(default='posts/thumbnails/squre_images/1.jpg', upload_to='posts/thumbnails/%Y/%m')),
                ('total_views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category')),
                ('tags', models.ManyToManyField(to='blog.tags')),
            ],
            options={
                'verbose_name': 'مقالات',
                'verbose_name_plural': 'مقالات',
                'ordering': ('-published_date',),
            },
        ),
        migrations.CreateModel(
            name='PostSEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog.post')),
            ],
        ),
        migrations.CreateModel(
            name='TagsSEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('tags_seo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posttags', to='blog.tags')),
            ],
        ),
    ]
