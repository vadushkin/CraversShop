from django.db import models

from .product import Product


class ProductOfTheDay(models.Model):
    quantity = models.PositiveIntegerField(
        verbose_name="Количество товаров",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="Продукт",
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    def __str__(self):
        return f'{self.pk} - {self.product}'

    class Meta:
        verbose_name = 'Продукт дня'
        verbose_name_plural = 'Продукты дня'
