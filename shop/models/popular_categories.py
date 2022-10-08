from django.db import models

from shop.models import Category


class PopularCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='Категория',
    )

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'Популярная Категория'
        verbose_name_plural = 'Популярные Категории'
