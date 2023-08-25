from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog
from blog.services import get_cache_blog


class BlogListView(ListView):
    model = Blog
    queryset = get_cache_blog()

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'text', 'image', 'is_published',)
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        """Создаю слаг"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """Веду количество просмотров"""
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'text', 'image', 'is_published')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        """Обновляю слаг"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


def toggle_published(request, pk):
    """Проверка публикации"""
    blog = get_object_or_404(Blog, pk=pk)
    if blog.is_published:
        blog.is_published = False
    else:
        blog.is_published = True

    blog.save()

    return redirect('blog:blog_list')
