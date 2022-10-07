from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .category import Category


class Blog(models.Model):
    # todo Набросок блога
    title = models.CharField(
        max_length=200,
        verbose_name="Название",
    )

    slug = models.SlugField(
        verbose_name="Слаг",
    )

    text = models.TextField(
        verbose_name="Текст",
    )

    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="Автор",
        editable=False,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name="Категория",
    )

    photo = models.ImageField(
        upload_to='our_services/',
        verbose_name='Фотография',
    )

    stars = models.CharField(
        max_length=1,
        choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)],
        default=1,
        verbose_name="Звёзды",
    )

    likes = models.IntegerField(
        default=0,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
    )

    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
