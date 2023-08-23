from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_published

app_name = BlogConfig.name

urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='detail_blog'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('is_published/<int:pk>/', toggle_published, name='is_published')
]
