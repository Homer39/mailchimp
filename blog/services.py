from django.conf import settings
from django.core.cache import cache

from blog.models import Blog


def get_cache_blog():
    queryset = Blog.objects.all()
    if settings.CACHE_ENABLE:
        key = 'category_list'
        blog_list = cache.get(key)
        if blog_list is None:
            blog_list = queryset
            cache.set(key, blog_list)
        return blog_list
    return queryset