from django.contrib.auth.models import User
from django.db import models

from .blog import Blog


class Comments(models.Model):
    # todo Это набросок коментов
    text = models.TextField(
        verbose_name="Текст комментария",
    )

    blog = models.ForeignKey(
        Blog,
        on_delete=models.DO_NOTHING,
        verbose_name="Блок",
    )

    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="Автор",
    )

    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    def __str__(self):
        return f'{self.author} - {self.blog}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментария'
