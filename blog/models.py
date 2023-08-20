from django.db import models

from mailing.models import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, unique=True, verbose_name='slug', **NULLABLE)
    text = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(verbose_name='Изображение', upload_to='blog/', **NULLABLE)
    creation_date = models.DateField(auto_now=True, auto_now_add=False, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
